a = int(input())
b = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
c = [0 for _ in range(a)]
for i in range(1, a + 1):
    d = i
    for e in b:
        while d % e == 0:
            c[e - 1] += 1
            d //= e
    if d != 1:
        c[d - 1] += 1
f = 1
g = 10 ** 9 + 7
for h in c:
    f *= (h + 1)
    f %= g
print(f)
