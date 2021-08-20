(l, r) = map(int, input().split())
a = min(r + 1, l + 2019)
b = 2019
for i in range(l, a):
    for j in range(l, a):
        if i == j:
            continue
        else:
            b = min(b, i * j % 2019)
print(b)
