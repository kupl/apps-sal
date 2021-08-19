(a, b) = input().split()
a = int(a)
b = int(b)
c = 0
for i in range(a, b + 1):
    if i // 10000 == i - i // 10 * 10 and i // 1000 - i // 10000 * 10 == i // 10 - i // 100 * 10:
        c = c + 1
print(c)
