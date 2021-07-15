n = int(input())
a = [int(i) for i in input().split()]
m = 10 ** 9
for x in range(n):
    s = 0
    for b in range(n):
        i = x + 1
        j = b + 1
        s += a[b] * ((abs(i - j) + j - 1 + i - 1) * 2)
    m = min(m, s)
print(m)
