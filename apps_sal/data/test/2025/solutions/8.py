q = int(input())
ans = [-1, -1, -1, -1, 1, -1, 1, -1, 2, 1, 2, -1, 3, 2, 3, 2, 4, 3, 4, 3]
for i in range(q):
    n = int(input())
    if n <= 19:
        print(ans[n])
    else:
        if n % 4 == 0:
            print(n // 4)
        if n % 4 == 1:
            print(n // 4 - 1)
        if n % 4 == 2:
            print(n // 4)
        if n % 4 == 3:
            print(n // 4 - 1)
