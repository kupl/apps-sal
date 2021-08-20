n = int(input())
a = 0
for i in range(1, n + 1, 2):
    c = 0
    for j in range(1, i + 1):
        if i % j == 0:
            c += 1
    if c == 8:
        a += 1
print(a)
