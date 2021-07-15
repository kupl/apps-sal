n = int(input())

m = n // 2 + 1

r = 1
c = 1
print(m)
for i in range(n):
    print(r, c)
    if i % 2 == 0:
        c += 1
    else:
        r += 1
