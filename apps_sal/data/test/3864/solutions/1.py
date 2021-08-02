A = [1, 6]
N = int(input())
mod = 998244353
for i in range(N + 2):
    A.append((4 * A[-1] + pow(4, i + 2, mod)) % mod)
B = [N * pow(2, N - 1, mod) % mod]
A[0] = 0
for i in range((N - 1) // 2):
    B.append(B[i] + A[i])
if N & 1:
    for i in range((N - 1) // 2):
        B.append(B[-i * 2 - 2])
else:
    for i in range((N - 1) // 2 + 1):
        B.append(B[-i * 2 - 1])
for i in range(N):
    B[i] = B[i] * pow(2, (mod - 2) * N, mod) % mod
print(*B, sep='\n')
