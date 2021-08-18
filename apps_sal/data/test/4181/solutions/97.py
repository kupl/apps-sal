N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

s = A[0]
ans = 0
for i in range(N):
    t = s if B[i] >= s else B[i]
    u = A[i + 1] if A[i + 1] <= (B[i] - t) else B[i] - t
    ans += t + u
    s = A[i + 1] - u

print(ans)
