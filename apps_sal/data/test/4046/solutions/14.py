n = int(input())
nums = [int(x) for x in input().split()]
res = [0]
for nu in nums:
    res.append(res[-1] + nu)
mi = min(res)
resp = [r - mi + 1 for r in res]
se = set(resp)
if max(resp) == len(resp) and len(resp) == len(se):
    print(*resp)
else:
    print(-1)
