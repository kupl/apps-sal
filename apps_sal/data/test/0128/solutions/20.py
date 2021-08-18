
n, k = [int(x) for x in input().split()]


if n == 1:
    print(0)
else:
    result = 0
    l = n
    for i in range(0, min(n // 2, k)):
        result += (l - 1) + (l - 2)
        l -= 2
    print(result)
