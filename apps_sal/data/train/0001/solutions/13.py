n = int(input())
for i in range(n):
    (a, b, c) = [int(el) for el in input().split()]
    if a > c or b > c:
        print(-1)
    elif a % 2 + b % 2 == 1:
        print(c - 1)
    elif a % 2 == b % 2 == c % 2:
        print(c)
    else:
        print(c - 2)
