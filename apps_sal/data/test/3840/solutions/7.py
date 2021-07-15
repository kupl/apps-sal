n = int(input())
A = [int(i) for i in input().split()]
if n == 1 or n % 2 == 0:
    print(-1)
    return
ans = 0
for i in range(n-1, 3, -2):
    diff = max(A[i], A[i-1])
    ans += diff
    A[(i-1)//2] -= diff
    A[(i-1)//2] = max(0, A[(i-1)//2])
ans += max(A[:3])
print(ans)

