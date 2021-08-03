import sys

n, k = map(int, input().split())

s = input().strip()

last = ''
count = 0
ans = {}

for c in s:
    if c != last:
        if last not in ans.keys():
            ans[last] = 0
        ans[last] += count // k
        last = c
        count = 1
    else:
        count += 1
if last not in ans.keys():
    ans[last] = 0
ans[last] += count // k
count = 1

print(max(ans.values()))
