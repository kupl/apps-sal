h = int(input())
c = 0
d = 0
while h > 1:
    h = h // 2
    c += 1
    d += 2**c
print(d + 1)
