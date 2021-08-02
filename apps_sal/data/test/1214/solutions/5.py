import math

n = int(input())
cl = list(map(int, input().split()))
sm = 0


def func(p, q):
    if q % 2 != 0 or q % 4 == 0:
        for i in range(int(math.sqrt(q)), 0, -1):
            if q % i == 0 and (i + q // i) % 2 == 0:
                k = ((q // i - i) // 2)**2
                if k > p:
                    return k - p
        return -1
    else:
        return -1


res = []

for i in range(n // 2):
    e = func(sm, cl[i])
    if e == -1:
        print('No')
        return
    res.append(e)
    res.append(cl[i])
    sm += e + cl[i]

print('Yes')
print(*res)
