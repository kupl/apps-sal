a = int(input())
b = int(input())
if a > b:
    (a, b) = (b, a)
i = 1
r = 0
while True:
    if a == b:
        print(r)
        break
    if b - a == 1:
        r += i
        print(r)
        break
    r += 2 * i
    i += 1
    b -= 2
