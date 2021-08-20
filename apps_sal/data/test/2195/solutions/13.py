T = int(input())
for _ in range(T):
    (x, y) = list(map(int, input().split()))
    if x < y:
        (x, y) = (y, x)
    (a, b) = list(map(int, input().split()))
    if b < a * 2:
        print(b * y + a * (x - y))
    else:
        print(a * (x + y))
