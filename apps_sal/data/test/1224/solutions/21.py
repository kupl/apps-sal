n = int(input())
a = 0
a3 = 1
while a3 < n:
    b = 0
    b5 = n - a3
    while b5 % 5 == 0:
        b5 //= 5
        b += 1
    if b5 == 1 and a != 0 and (b != 0):
        print(a, b)
        break
    else:
        a += 1
        a3 *= 3
else:
    print(-1)
