from collections import defaultdict


def process_letter(nums):
    d = {}
    for i in range(26):
        assert chr(ord('a') + i).islower()
        d[chr(ord('a') + i)] = nums[i]
    return d


dic = process_letter([int(x) for x in input().split()])
s = input()
current = 0
value = defaultdict(int)
ans = 0
for c in s:
    ans += value[c, current]
    current += dic[c]
    value[c, current] += 1
print(ans)
