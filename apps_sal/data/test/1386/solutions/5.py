import sys

w,h = list(map(int, sys.stdin.readline().strip().split()))

p = 998244353
b = w + h
a = 2
ans = 1
while b > 0:
    if b % 2 == 1:
        b = b - 1
        ans = (ans * a) % p
    else:
        b = b // 2
        a = (a * a) % p
print(ans)
