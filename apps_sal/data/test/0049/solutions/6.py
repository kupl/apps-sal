a = int(input())
c = [1] * 30
for i in range(1, 20):
    c[i] = 9 * i * pow(10, i - 1)
for i in range(1, 15):
    if (a > c[i]):
        a -= c[i]
    else:
        d = int((a - 1) / i + pow(10, i - 1) - 1)
        e = (a - 1) % i + 1
        f = str(d + 1)
        print(f[e - 1])
        return
