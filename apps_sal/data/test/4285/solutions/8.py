mod = 10**9 + 7
N, = list(map(int, input().split()))
s = input().strip()
a = 0
b = 0
c = 0
t = 1
for i in range(N):
    if s[i] == "a":
        a = (a + t) % mod
    elif s[i] == "b":
        b = (b + a) % mod
    elif s[i] == "c":
        c = (c + b) % mod
    elif s[i] == "?":
        t, a, b, c = t * 3 % mod, (a * 3 + t) % mod, (b * 3 + a) % mod, (c * 3 + b) % mod
print(c)
