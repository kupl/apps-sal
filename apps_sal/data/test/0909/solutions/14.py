a = int(input())
b = int(input())
c = int(input())
if a != 1 and b != 1 and c != 1:
    print(a * b * c)
elif a != 1 and b == 1 and c != 1:
    m = max(a, c)
    n = min(a, c)
    print((n + b) * m)
elif a == 1 and c == 1:
    print(a + b + c)
elif a != 1 and c == 1:
    print(a * (b + c))
elif a == 1 and c != 1:
    print((a + b) * c)
