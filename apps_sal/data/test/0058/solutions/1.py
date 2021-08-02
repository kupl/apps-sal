n = int(input())
a = int(input())
b = int(input())

c = 1
rem = n
a1, b1 = 0, 0
while True:
    if rem >= a and a1 < 4:
        rem -= a
        a1 += 1
    if rem >= b and b1 < 2:
        rem -= b
        b1 += 1
    if a1 == 4 and b1 == 2:
        print(c)
        break
    if (rem < a or a1 == 4) and (rem < b or b1 == 2):
        rem = n
        c += 1
