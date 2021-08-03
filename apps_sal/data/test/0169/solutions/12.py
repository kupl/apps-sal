

n = int(input())
a = int(input())
b = int(input())
c = int(input())

if b > n and a > n:
    print(0)
elif b - c >= a or b > n:
    print(n // a)
else:
    print((n - b) // (b - c) + 1 + (c + (n - b) % (b - c)) // a)
