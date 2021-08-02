P, a = 998244353, 1
n = int(input())
d = list(map(int, input().split()))
s = sum(d) % P
for i in d:
    a *= i
    a %= P
for i in range(n, 2 * n - 2):
    a *= s - i
    a %= P
print(a)
