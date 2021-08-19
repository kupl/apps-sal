n = int(input())
a = list(map(int, input().split()))
x = sum(a)
a += a
an = 0
ann = 1000000
for j in range(n):
    an = 0
    for i in range(j, 2 * n):
        an += a[i]
        if an >= x // 2:
            if abs(x - 2 * an) < abs(x - 2 * ann):
                ann = an
            an = 0
print(abs(x - 2 * ann))
