N = int(input())
c = (N + 1) * [0]

for i in range(2, N + 1):
    j = 2
    while j * j <= i:
        while i % j == 0:
            c[j] += 1
            i //= j
        j += 1
    if 1 < i:
        c[i] += 1


def f(x): return sum(y + 1 >= x for y in c)


print(f(75) + f(25) * (f(3) - 1) + f(15) * (f(5) - 1) + f(5) * (f(5) - 1) // 2 * (f(3) - 2))
