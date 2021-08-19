(n, m) = list(map(int, input().split()))
a = input()
b = input()
if n < m:
    a = '0' * (m - n) + a
elif m < n:
    b = '0' * (n - m) + b
n = max(n, m)
tot = 0
sm = 0
for i in range(n):
    if b[i] == '1':
        tot += 1
    if a[i] == '1':
        sm = (sm + tot * int(pow(2, n - i - 1, 998244353))) % 998244353
print(sm)
