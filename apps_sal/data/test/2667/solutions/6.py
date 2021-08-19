try:
    N = int(input())
    lst = sorted(list(map(int, input().split())))
    sum = 0
    for i in range(N):
        sum = sum + lst[i]
    sum2 = 0
    for i in range(1, N + 1):
        sum2 = sum2 + i
    if sum2 == sum:
        print('YES')
    else:
        print('NO')
except:
    pass
