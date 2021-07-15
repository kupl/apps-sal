A, B = list(map(int, input().split()))

m = len(format(B, "b"))

a = A
b = B
AA = 0
BB = 0

if A % 2 == 1:
    a = A + 1
    AA = A
if B % 2 == 0:
    b = B - 1
    BB = B
b += 1

t = (b - a) // 2
#print(AA, b, t)
if t % 2 == 0:
    print((AA ^ BB))
else:
    print((AA ^ BB ^ 1))

