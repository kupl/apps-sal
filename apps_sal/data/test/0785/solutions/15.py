
import sys

try:
    while True:
        n, a, b = list(map(int, input().split(" ")))
        flag = False
        if a > b:
            flag = True
            a, b = b, a
        if 6 * n <= a * b:
            print(a * b)
            res = str(a) + " " + str(b)
            print(res)
            continue
        res = 1 << 60
        i = a
        ans1 = 0
        ans2 = 0
        while i * i <= 6 * n:
            tmp = 6 * n // i
            if tmp * i < 6 * n:
                tmp += 1
            if tmp < b:
                i += 1
                continue
            if i * tmp < res:
                res = i * tmp
                ans1 = i
                ans2 = tmp
            i += 1
        if flag:
            ans1, ans2 = ans2, ans1
        print(res)
        ans = str(ans1) + " " + str(ans2)
        print(ans)


except EOFError:
    pass
