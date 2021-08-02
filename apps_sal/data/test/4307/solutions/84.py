n = input()
n = int(n)
s = 0
for i in range(1, n + 1):
    p = 0
    if i % 2 == 0:
        continue
    for j in range(1, i + 1):
        if i % j == 0:
            p += 1
    if p == 8:
        s += 1
print(s)
