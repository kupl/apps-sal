n = int(input())
a = list(map(int, input().split()))
b = [0] * n
c = []
for i in range(n - 1, -1, -1):
    v = i + 1
    s = 0
    for j in range(1, 10 ** 6):
        if v * j > n:
            break
        s += b[v * j - 1]
    if s % 2 != a[i]:
        b[i] = 1
        c.append(v)
print(len(c))
for i in reversed(c):
    print(i)
