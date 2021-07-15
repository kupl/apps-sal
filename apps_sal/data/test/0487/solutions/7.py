n = int(input())
a = [int(i) for i in input().split()]
c = max(a)
while True:
    x = 0
    y = 0
    for el in a:
        x += el
        y += c - el
    if x < y:
        break
    c += 1
print(c)

