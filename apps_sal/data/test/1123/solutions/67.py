def left_bin(a, n, c):
    ns = [int(i) for i in bin(n)[3:]]
    t = a
    for i in ns:
        t = t * t % c
        if i == 1:
            t = t * a % c
    return t


(n, k) = list(map(int, input().split()))
c = 10 ** 9 + 7
tm = [0] + [1] * k
a = k // 2
ans = k * (k + 1) // 2 - a * (a + 1) // 2
for i in range(k // 2, 0, -1):
    a = k // i
    t = (left_bin(a, n, c) - sum([tm[j * i] for j in range(2, a + 1)])) % c
    ans = (ans + t * i) % c
    tm[i] = t
print(ans)
