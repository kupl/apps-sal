n = int(input())
print(n // 2 + 1)
r = 1
c = 1
for i in range(n):
    print(r, c)
    if i % 2 == 0:
        c += 1
    else:
        r += 1
