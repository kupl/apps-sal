n = int(input())
a = [int(i) for i in input().split()]
a_max = max(a)
i_max = a.index(a_max) + 1
a_min = min(a)
i_min = a.index(a_min) + 1
ans = []
if a_min >= 0:
    print(n - 1)
    for i in range(1, n):
        print((i, i + 1))
elif a_max < 0:
    print(n - 1)
    for i in range(n, 1, -1):
        print((i, i - 1))
elif abs(a_max) > abs(a_min):
    print(2 * n - 2)
    for i in range(1, n + 1):
        if i != i_max:
            print((i_max, i))
    for i in range(1, n):
        print((i, i + 1))
else:
    print(2 * n - 2)
    for i in range(1, n + 1):
        if i != i_min:
            print((i_min, i))
    for i in range(n, 1, -1):
        print((i, i - 1))
