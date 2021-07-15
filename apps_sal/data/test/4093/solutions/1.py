t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    if n == 1:
        res = 0
    elif n == 2:
        res = m
    else:
        res = 2 * m
    print(res)

