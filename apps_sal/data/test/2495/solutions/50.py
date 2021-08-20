def ARC072C():
    N = int(input())
    a = list(map(int, input().split()))
    cnt1 = 0
    cnt2 = 0
    sum1 = a[0]
    sum2 = a[0]
    if sum1 <= 0:
        cnt1 = 1 - a[0]
        sum1 = 1
    if sum2 >= 0:
        cnt2 = abs(-1 - a[0])
        sum2 = -1
    j = 1
    for i in range(1, N):
        sum1 += a[i]
        sum2 += a[i]
        if j % 2 == 0:
            if sum1 <= 0:
                cnt1 += 1 - sum1
                sum1 = 1
            if sum2 >= 0:
                cnt2 += abs(-1 - sum2)
                sum2 = -1
        else:
            if sum1 >= 0:
                cnt1 += abs(-1 - sum1)
                sum1 = -1
            if sum2 <= 0:
                cnt2 += 1 - sum2
                sum2 = 1
        j += 1
    print(min(cnt1, cnt2))


ARC072C()
