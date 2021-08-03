N = int(input())

A = [int(x) for x in input().split()]

ans = 0
A.sort(reverse=True)
# print(A)
ans += sum(A[:(N + 1) // 2 - 1])
for i in range((N + 1) // 2 - 1):
    ans += min(A[i], A[i + 1])

if N % 2 == 0:
    ans += A[N // 2 - 1]

print(ans)
