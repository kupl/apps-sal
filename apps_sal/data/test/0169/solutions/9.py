n = int(input())
a = int(input())
b = int(input())
c = int(input())
if (a <= b - c):
    print(n // a)
    return
otv = n // (b - c)
razn = b - c
razn1 = n - b
if ((razn1 // razn) >= 0):
    otv = razn1 // razn + 1
else:
    otv = 0
otv += (n - otv * (b - c)) // a
print(otv)
