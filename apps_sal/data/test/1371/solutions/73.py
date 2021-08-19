s = int(input())
mod = 10 ** 9 + 7
A = [0, 0, 0, 1] + [0] * 2000
for i in range(4, s + 1):
    A[i] = (A[i - 1] + A[i - 3]) % mod
print(A[s])
