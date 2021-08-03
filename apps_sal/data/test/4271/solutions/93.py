N = int(input())
A = [int(n) for n in input().split()]
B = [int(n) for n in input().split()]
C = [int(n) for n in input().split()]

ans = sum(B)
for i in range(N - 1):
    if A[i + 1] - A[i] == 1:
        ans += C[A[i] - 1]

print(ans)
