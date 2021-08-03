a = int(input())
while a > 0:
    b = [int(i)for i in input().split()]
    c = 0
    while b[0] * b[1] != 0:
        c += b[1] // b[0]
        b[0], b[1] = b[1] % b[0], b[0]
    print(c)
    a -= 1
