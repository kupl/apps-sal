n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(a[0])
else:
    prod_minus = False
    for i in range(n - 1):
        if a[i] * a[i + 1] <= 0:
            prod_minus = True
            break
    Min_abs = float("inf")
    Sum = 0
    for num in a:
        Sum += abs(num)
        if abs(num) < Min_abs:
            Min_abs = abs(num)

    if prod_minus:
        print(Sum)
    else:
        print(Sum - 2 * Min_abs)
