q = int(input())
N = [int(input()) for i in range(q)]
t = [3 ** i for i in range(10)]


def d(x):
    ans = 0
    m = 1
    while x > 0:
        if x % 2 == 1:
            ans += m
        m *= 3
        x //= 2
    return ans


for i in range(q):
    n = N[i]
    m = 0
    t = 0
    while m < n:
        m = d(t)
        t += 1
    print(m)
