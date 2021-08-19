n = int(input())
s = (n + 1) * n // 4
a = []
for i in range(n, 0, -1):
    if s >= i:
        a.append(i)
        s -= i
print(abs((n + 1) * n // 2 - sum(a) - sum(a)))
print(len(a), end=' ')
for x in a:
    print(x, end=' ')
