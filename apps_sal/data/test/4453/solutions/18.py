import sys


def I():
    return sys.stdin.readline().rstrip()


q = int(I())
for _ in range(q):
    n = int(I())
    c = [-1] * n

    def getp(i):
        s = []
        while c[i] >= 0:
            s.append(i)
            i = c[i]
        for j in s:
            c[j] = i
        return i
    p = list(map(int, I().split()))
    p = [i - 1 for i in p]
    for i, q in enumerate(p):
        a, b = getp(i), getp(q)
        if a != b:
            c[a] += c[b]
            c[b] = a
    for i in p:
        print(-c[getp(i)], end=" ")
    print()
