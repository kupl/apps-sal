t = int(input())
for _ in range(t):
    (a, b) = list(map(int, input().split()))
    if a == b:
        print(0)
    elif b - a > 0 and (b - a) % 2 != 0:
        print(1)
    elif b - a > 0 and (b - a) % 2 == 0:
        print(2)
    elif a - b > 0 and (b - a) % 2 == 0:
        print(1)
    elif a - b > 0 and (b - a) % 2 != 0:
        print(2)
