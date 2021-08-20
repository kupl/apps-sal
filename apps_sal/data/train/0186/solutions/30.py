def prune(costs):
    ans = []
    for (ind, elem) in enumerate(costs):
        if any((costs[i] + costs[j] == elem for i in range(ind) for j in range(ind))):
            pass
        else:
            ans.append(elem)
    return ans


def find_longest_combos(costs, start, prefix, left, max_yets):
    if start == len(costs):
        if left == 0 and len(prefix) >= max_yets[0]:
            max_yets[0] = len(prefix)
            yield prefix[:]
    else:
        theoretical_max_length = len(prefix) + left // costs[start]
        if theoretical_max_length < max_yets[0]:
            return
        if costs[start] <= left:
            prefix.append(costs[start])
            yield from find_longest_combos(costs, start, prefix, left - costs[start], max_yets)
            prefix.pop()
        if True:
            yield from find_longest_combos(costs, start + 1, prefix, left, max_yets)


def rlencode(arr):
    ans = []
    for elem in arr:
        if ans and ans[-1][0] == elem:
            ans[-1] = (ans[-1][0], ans[-1][1] + 1)
        else:
            ans.append((elem, 1))
    return ans


def encode(digit_choices, combo):
    return sorted([(digit_choices[elem], freq) for (elem, freq) in combo], reverse=True)


def write(rle):
    ans = []
    for (elem, freq) in rle:
        for _ in range(freq):
            ans.append(elem)
    return ''.join(map(str, ans))


def gcd(a, b):
    (a, b) = (min(a, b), max(a, b))
    while a > 0:
        (a, b) = (b % a, a)
    return b


def gcdall(arr):
    ans = arr[0]
    for elem in arr:
        ans = gcd(ans, elem)
    return ans


def obviously_unsatisfactory(cost, target):
    if min(cost) > target:
        return True
    if target % gcdall(cost) != 0:
        return True
    return False


def largest_num(cost, target):
    if obviously_unsatisfactory(cost, target):
        return '0'
    costs = sorted(list(set(cost)))
    costs = prune(costs)
    combinations = list(find_longest_combos(costs, 0, [], target, [0]))
    if not combinations:
        return '0'
    max_length = max(map(len, combinations))
    combinations = (c for c in combinations if len(c) == max_length)
    digit_choices = {}
    for (i, c) in enumerate(cost):
        digit_choices[c] = i + 1
    combinations = map(rlencode, combinations)
    combinations = (encode(digit_choices, combo) for combo in combinations)
    return write(max(combinations))


class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:
        return largest_num(cost, target)
