import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = 998244353
a = a[::-1]
s = a[0]
for i in range(1, n):
    s += a[i] * pow(2, i - 1, m) * (i + 2) % m
    s = s % m
print(s % m)
