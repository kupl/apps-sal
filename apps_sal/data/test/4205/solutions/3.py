import copy
N = int(input())
p = list(map(int, input().split()))
pcopy = copy.deepcopy(p)
ans = sorted(p)

is_ascend = False
if p == ans:
    is_ascend = True

for i in range(N):
    for j in range(i+1,N):
        p = copy.copy(pcopy)
        p[i], p[j] = p[j], p[i]
        if p == ans:
            is_ascend = True

if is_ascend:
    print("YES")
else:
    print("NO")

