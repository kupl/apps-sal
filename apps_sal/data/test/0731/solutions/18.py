p = input().split()
w = int(p[0])
m = int(p[1])
a = m
cost = int(p[2])
c = 0
while m != 0:
    m = m // 10
    c = c + 1
sum = 0
x = 10 ** c - a
if cost * c * x >= w:
    print(w // (cost * c))
else:
    sum = sum + x
    w = w - cost * c * x
    for i in range(c + 1, 18):
        y = 9 * 10 ** (i - 1)
        if y * i * cost >= w:
            break
        else:
            w = w - cost * y * i
            sum = sum + y
    print(sum + w // (cost * i))
