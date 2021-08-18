import sys
N = int(input())
lsA = list(map(int, input().split()))
if 0 in lsA:
    print(0)
    return
ans = 1
for i in range(N):
    ans *= lsA[i]
    if ans > 10 ** 18:
        print(-1)
        return
print(ans)
