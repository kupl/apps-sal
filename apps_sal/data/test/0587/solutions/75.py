import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
nums = []
for i in range(N):
    t, d = list(map(int, input().split()))
    nums.append((d, t))
nums.sort(reverse=True)
se = set()
doubled = []
rest = []
points = 0
for i, n in enumerate(nums):
    if i < K:
        if not n[1] in se:
            se.add(n[1])
        else:
            doubled.append(n)
        points += n[0]
    else:
        rest.append(n)
ans = points + pow(len(se), 2)
idx = len(doubled) - 1
for d, t in rest:
    if idx < 0:
        break
    if t in se:
        continue
    points -= doubled[idx][0]
    idx -= 1
    points += d
    se.add(t)
    ans = max(ans, points + pow(len(se), 2))
print(ans)
