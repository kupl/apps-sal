def digitsum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


for nitish in range(int(input())):
    ans = 10 ** 30
    str_arr = input().split(' ')
    arr = [int(num) for num in str_arr]
    n = arr[0]
    k = arr[1]
    for lastdigit in range(10):
        for numberofnine in range(100):
            if numberofnine * 9 + lastdigit > n:
                break
            s = ''
            for x in range(numberofnine):
                s += '9'
            s += str(lastdigit)
            xx = int(s)
            done = 0
            for j in range(k + 1):
                done += digitsum(xx + j)
            done -= max(0, k + 1 - (10 - lastdigit))
            if done > n:
                continue
            for aurek in range(9):
                p = min(k + 1, 10 - lastdigit)
                ddone = done + aurek * p + (aurek + 1) * (k + 1 - p)
                if ddone > n:
                    continue
                if ddone == n:
                    if aurek > 0:
                        s = str(aurek) + s
                        ans = min(ans, int(s))
                    else:
                        ans = min(ans, int(s))
                    continue
                ddone = n - ddone
                if ddone % (k + 1) != 0:
                    continue
                ddone //= k + 1
                t = ddone % 9
                ss = ''
                if t:
                    ss += str(t)
                for jj in range(ddone // 9):
                    ss += '9'
                if len(ss) > 0:
                    ss += str(aurek)
                if len(ss) == 0:
                    ans = min(ans, xx)
                else:
                    ss += s
                    ans = min(ans, int(ss))
    if ans == 10 ** 30:
        ans = -1
    print(ans)
