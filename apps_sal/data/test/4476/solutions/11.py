T = int(input())
for t in range(T):
    (a, b) = list(map(int, input().split()))
    res = 0
    if b > a:
        if b % 2 != a % 2:
            res = 1
        else:
            res = 2
    elif b < a:
        if b % 2 == a % 2:
            res = 1
        else:
            res = 2
    print(res)
