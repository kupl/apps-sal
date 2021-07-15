n, m = map(int, input().split())
p = [input() for i in range(n)]
t = [0] * m
k = 0
for i in range(1, n + 1):
    s = 0
    for j in range(1, m + 1):
        s += t[-j]
        q = s + 2 * (p[-i][-j] == 'W') - 1
        t[-j] -= q
        s -= q
        if q: k += 1
print(k)
