n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
c = dict()

for i in a:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1

c = sorted(list(c.values()))


def check(p):
    d = c[:]
    for _ in range(n):
        while d and d[-1] < p:
            del d[-1]
        if not d:
            return False
        d[-1] -= p
    return True


for k in range(m, -1, -1):
    if check(k):
        print(k)
        break
else:
    print(0)
