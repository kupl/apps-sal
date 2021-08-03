N = input()

B = [int(i) for i in input().split()]

a, b = 0, 0

for i in B:
    if i % 2 == 0:
        b = b + 1
    else:
        a = a + 1


if a <= b:
    print(a)
else:
    a = a - b
    print(b + a // 3)
