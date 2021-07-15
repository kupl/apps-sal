T = int(input())

for _ in range(T):
    n, m = list(map(int, input().split()))
    time, mx, mn = 0, m, m
    flag = True

    for __ in range(n):
        x, y, z = list(map(int, input().split()))

        if not flag:
            continue

        mx += x - time
        mn -= x - time

        if mx < y or mn > z:
            flag = False

        if mx > z:
            mx = z

        if mn < y:
            mn = y

        time = x

    print('YES' if flag else 'NO')

