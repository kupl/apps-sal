class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        s = list(s)
        if len(s) < 2:
            return 0
        if len(s) == len(set(s)):
            return 0
        total = 0
        while True:
            i = 0
            deleted = False
            for (_, group) in itertools.groupby(s):
                group = list(group)
                if len(group) > 1:
                    (idx_max, max_cost) = (-1, -1)
                    for (j, c) in enumerate(cost[i:i + len(group)]):
                        if c == None:
                            continue
                        if c > max_cost:
                            max_cost = c
                            idx_max = i + j
                    subtotal = 0
                    for j in range(i, i + len(group)):
                        if j == idx_max:
                            continue
                        subtotal += cost[j]
                        cost[j] = None
                        s[j] = None
                    total += subtotal
                    deleted = True
                i += len(group)
            if deleted:
                s = [c for c in s if c != None]
                cost = [c for c in cost if c != None]
            else:
                break
        return total


def has_two_consecutive_chars(s: str) -> bool:
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            return True
    return False
