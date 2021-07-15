for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    ar = [[0, -10 ** 9, 10 ** 9]]
    for ______ in range(n):
        ar.append(list(map(int, input().split())))
    ar.sort()
    left, right = m, m
    ans = 'YES'
    for i in range(1, n + 1):
        left -= ar[i][0] - ar[i - 1][0]
        right += ar[i][0] - ar[i - 1][0]
        left, right = [max(left, ar[i][1]), min(right, ar[i][2])]
        if right - left < 0:
            ans = 'NO'
    print(ans)
