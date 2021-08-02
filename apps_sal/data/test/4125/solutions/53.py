from math import gcd
N, X = map(int, input().split())
x = list(map(int, input().split()))

if N == 1:
    print(abs(X - x[0]))

else:
    l = []
    for i in range(N):
        l_ = abs(X - x[i])
        l.append(l_)
    # print(l)
    ans = l[0]
    for i in range(1, len(l)):
        ans = gcd(ans, l[i])

    print(ans)
