N, K = map(int, input().split())
A = [i for i in range(N + 1)]
mod = 10**9 + 7
ans = 0
head = sum(A[:K - 1]) if K > 1 else 0
tail = sum(A[-K + 1:]) if K > 1 else 0
for i in range(K, N + 2):
    head += A[i - 1]
    tail += A[-i]
    ans += tail - head + 1
    ans = ans % mod

print(ans)
