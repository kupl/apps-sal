n, a, b, c = list(map(int, input().split()))
k = 4 - (n % 4)
if k == 4:
    print(0)
elif k == 1:
    print(min(a, c * 3, b + c))
elif k == 2:
    print(min(2 * a, b, 2 * c))
elif k == 3:
    print(min(3 * a, c, b + a))

