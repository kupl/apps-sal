t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    fbp = n - 2
    cur = 1
    while cur < k:
        k -= cur
        fbp -= 1
        cur += 1
    sbp = n - k
    cnt = 0
    for j in range(n):
        if j == fbp:
            print('b', end='')
        elif j == sbp:
            print('b', end='')
        else:
            print('a', end='')
    print()
