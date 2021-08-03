from collections import defaultdict


def can_remove(a, n):
    nums = defaultdict(lambda: 0)

    for i in range(n, len(a)):
        nums[a[i]] += 1

    if all([x <= 1 for x in list(nums.values())]):
        return True

    for remove_num in range(n, len(a)):
        nums[a[remove_num]] -= 1
        nums[a[remove_num - n]] += 1
        if all([x <= 1 for x in list(nums.values())]):
            return True

    return False


n = int(input())
a = list(map(int, input().split()))

impossible = -1
possible = len(a) - 1

while possible - impossible > 1:
    m = (possible + impossible) // 2
    if can_remove(a, m):
        possible = m
    else:
        impossible = m

print(possible)
