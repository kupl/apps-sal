N = int(input())
A = list(map(int, input().split()))
ans = 1
if 0 in A:
    print(0)
    return

for i in range(N):
    ans *= A[i]
    if ans > 10**18:
        print(-1)
        return

print(ans)
