def gcd(a, b):
    while a % b != 0:
        t = b
        b = a % b
        a = t
    return b


def lcm(a, b):
    return a * b // gcd(a, b)


for _ in range(int(input())):
    n = int(input())
    tickets = list(map(int, input().split()))
    (x, a) = list(map(int, input().split()))
    (y, b) = list(map(int, input().split()))
    k = int(input())
    lcmab = lcm(a, b)
    if y < x:
        (x, y) = (y, x)
        (a, b) = (b, a)
    tickets.sort(reverse=True)
    pfsums = [0] * (n + 1)
    ans = -1
    for i in range(1, n + 1):
        pfsums[i] = pfsums[i - 1] + tickets[i - 1]
        streak = i // lcmab
        xprof = i // a - streak
        yprof = i // b - streak
        mylen = i
        if mylen >= streak:
            got = pfsums[streak] * (x + y) // 100
            mylen -= streak
        else:
            got = (pfsums[mylen] - pfsums[streak]) * (x + y) // 100
            if got >= k:
                ans = i
                break
        if mylen >= yprof:
            got += (pfsums[streak + yprof] - pfsums[streak]) * y // 100
            mylen -= yprof
        else:
            got += (pfsums[streak + mylen] - pfsums[streak]) * y // 100
            if got >= k:
                ans = i
                break
        if mylen >= xprof:
            got += (pfsums[streak + yprof + xprof] - pfsums[streak + yprof]) * x // 100
            mylen -= xprof
        else:
            got += (pfsums[streak + mylen + yprof] - pfsums[streak + yprof]) * x // 100
        if got >= k:
            ans = i
            break
    print(ans)
