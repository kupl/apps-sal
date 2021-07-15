n = int(input())
for i in range(n):
    a,b = list(map(int, input().split()))
    a1 = a
    if a % 2 == 0:
        a1 += 1
    b1 = b
    if b % 2 == 0:
        b1 -= 1
    n = 0
    if a1 <= b1:
        num = (b1 - a1) // 2 + 1
        n = num * (b1 + a1) // 2
        n *= -1
    b2 = b
    a2 = a
    if a % 2 == 1:
        a2 += 1
    if b % 2 == 1:
        b2 -= 1
    n2 = 0
    if a2 <= b2:
        num = (b2 - a2) // 2 + 1
        n2 = num * (b2 + a2) // 2
    print(n + n2)


