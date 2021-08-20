n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
mod = 998244353
AX = []
for i in range(n):
    AX.append(A[i] * (i + 1) * (n - i))
AX.sort()
B.sort(reverse=True)
ANS = 0
for i in range(n):
    ANS = (ANS + AX[i] * B[i]) % mod
print(ANS)
