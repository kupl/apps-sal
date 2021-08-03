t, k = input(), int(input())
s, n, d = 0, 1, 1000000007
for i in t:
    if i in '05':
        s += n
    n = (n << 1) % d
p = (pow(n, k, d) - 1) * pow(n - 1, d - 2, d)
print((p % d) * (s % d) % d)
