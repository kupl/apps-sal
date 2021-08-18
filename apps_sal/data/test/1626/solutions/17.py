
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 1

for i in range(n // k):
    count = 1 + (10**k - 1) // A[i]
    count -= (10**(k - 1) * (B[i] + 1) - 1) // A[i] - (10**(k - 1) * B[i] - 1) // A[i]

    ans = ans * count % (10**9 + 7)

print(ans)
