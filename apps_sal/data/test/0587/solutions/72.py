import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
nums = [[] for i in range(N)]
for i in range(N):
    t, d = list(map(int, input().split()))
    t -= 1
    nums[t].append(d)
maxs = []
rest = []
for i in range(N):
    if len(nums[i]) == 0: continue
    nums[i].sort(reverse=True)
    maxs.append(nums[i][0])
    for n in nums[i][1:]:
        rest.append(n)
maxs.sort(reverse=True)
rest.sort(reverse=True)
if len(maxs) > K:
    maxs = maxs[:K]
other = []
idx = 0
while len(maxs)+len(other) < K:
    other.append(rest[idx])
    idx += 1
rest = rest[idx:]

types = len(maxs)
for i,r in enumerate(rest):
    diff = types*types - pow(types-1, 2)
    if diff < r-maxs[len(maxs)-1-i]:
        maxs[len(maxs)-1-i] = r
        types -= 1
    else:
        break
ans = types*types
for num in maxs:
    ans += num
for num in other:
    ans += num
print(ans)

