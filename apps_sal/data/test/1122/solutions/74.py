N, M = map(int, input().split())

if N % 2 == 1:
    for i in range(1, M + 1):
        l = i
        r = N - i
        print(l, r)
else:
    flag = False
    l = 1
    r = N - 1
    cnt = 0
    while cnt < M:
        if not flag and r - l <= N // 2:
            r -= 1
            flag = True
        print(l, r)
        l += 1
        r -= 1
        cnt += 1
