T = int(input())
for _ in range(T):
    n = int(input())
    aa = list(map(int, input().split()))
    evens = 0
    odds = 0
    aa.sort()
    ba = -100
    cnt = 0
    for a in aa:
        if a % 2 == 0:
            evens += 1
        else:
            odds += 1
        if abs(a - ba) == 1:
            cnt += 1
            ba = -100
        else:
            ba = a
    evens %= 2
    odds %= 2
    if evens == 0 and odds == 0:
        print('YES')
    elif cnt >= 1:
        print('YES')
    else:
        print('NO')
