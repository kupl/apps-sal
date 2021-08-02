N = int(input())
A = list(map(int, input().split()))
ans = 1
A.sort()

for i in range(N):
    ans *= A[i]
    if ans > 1e18:
        print(-1)
        break
else:
    print(ans)
