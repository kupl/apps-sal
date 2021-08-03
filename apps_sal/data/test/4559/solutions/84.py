n = int(input())

A = list(map(int, input().split()))
A.sort()

ans = int(1)

for i in range(n):
    ans *= A[i]
    if ans > 1e18:
        print(-1)
        return
print(ans)
