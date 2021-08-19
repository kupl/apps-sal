import sys
input = sys.stdin.readline
'\na,b=[],[]\nfor i in range(n):\n    A, B = map(int, input().split())\n    a.append(A)   \n    b.append(B)'


def premf(n):
    IsPrime = [False] + [False] + [True] * (n - 1)
    res = []
    for j in range(4, n + 1, 2):
        IsPrime[j] = False
    for i in range(1, n + 1, 2):
        if IsPrime[i]:
            for j in range(i * 2, n + 1, i):
                IsPrime[j] = False
            if IsPrime[(i + 1) // 2]:
                res.append(i)
    return res


q = int(input())
n = 10 ** 5
res = premf(n)
a = [0] * (10 ** 5 + 1)
t = 0
for i in range(len(res)):
    t += 1
    a[res[i]] = t
for i in range(10 ** 5):
    if a[i + 1] == 0:
        a[i + 1] = a[i]
for i in range(q):
    (l, r) = map(int, input().split())
    print(a[r] - a[l - 1])
