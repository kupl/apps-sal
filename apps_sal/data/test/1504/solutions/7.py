import sys
input = sys.stdin.readline
T = int(input())

for testcase in range(1, T + 1):
    n, k = list(map(int, input().split()))
    a, b = list(map(int, input().split()))
    s, t = list(map(int, input().split()))

    if a > s:
        a, s = s, a
        b, t = t, b
    """ a <= s """

    if s <= b and n * (min(b, t) - s) >= k:
        print(0)
    else:
        if s <= b:
            now = n * (min(b, t) - s)
            w = n * ((s - a) + abs(t - b))
            if now + w >= k:
                print(k - now)
            else:
                now += w
                print(w + (k - now) * 2)
        else:
            if (t - a) >= k:
                print(s - b + k)

            else:
                res = 10**20
                for i in range(1, n + 1):
                    tmp = i * (s - b)
                    if i * (t - a) >= k:
                        tmp += k
                        # print("b",i,a,b,s,t)
                    else:
                        tmp += i * (t - a) + (k - i * (t - a)) * 2
                    res = min(res, tmp)
                    # print("a",i,tmp)
                print(res)
