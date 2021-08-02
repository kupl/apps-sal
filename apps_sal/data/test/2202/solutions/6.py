n, p = list(map(int, input().split()))
pre = [0] * 100100
A = list(map(int, input().split()))
for i in range(n):
    pre[i + 1] = (pre[i] + A[i]) % p
print(max((pre[i] - pre[0]) % p + (pre[n] - pre[i]) % p for i in range(1, n)))
