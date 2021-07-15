for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s1, s2, last, q1, q2, flag = [], [], 0, 0, n-1, 0
    while q1 <= q2:
        sum1 = 0
        while sum1 <= last and q1 <= q2:
            if flag == 0:
                sum1 += a[q1]
                q1 += 1
            else:
                sum1 += a[q2]
                q2 -= 1
        if flag == 0:
            s1.append(sum1)
        else:
            s2.append(sum1)
        flag, last = 1-flag, sum1
    print(len(s1)+len(s2), sum(s1), sum(s2))

