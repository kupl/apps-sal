t = int(input())
for i in range(t):
    (b, p, f) = list(map(int, input().split()))
    (h, c) = list(map(int, input().split()))
    if h > c:
        num = min(b // 2, p)
        b -= num * 2
        num2 = min(b // 2, f)
        print(num * h + num2 * c)
    else:
        num = min(b // 2, f)
        b -= num * 2
        num2 = min(b // 2, p)
        print(num * c + num2 * h)
