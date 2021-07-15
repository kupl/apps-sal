# http://codeforces.com/contest/884/problem/C
# unsolved
from functools import lru_cache

n = int(input())
p = list(map(int, input().split()))

l = []
score = 0
jeden = 0
dwa = 0


@lru_cache(maxsize=10000)
def wzor(s):
    return s * s


for i in range(n):

    if p[i] != 0:
        start = i
        end = p[i]
        lenght = 0
        k = 0

        if start + 1 != p[i]:

            while k - 1 != start:
                k = end
                end = p[end - 1]
                p[k - 1] = 0
                lenght += 1

        else:
            p[end - 1] = 0
            lenght += 1

        if lenght > jeden:
            l.append(dwa)
            dwa = jeden
            jeden = lenght

        elif lenght > dwa:
            l.append(dwa)
            dwa = lenght

        else:
            l.append(lenght)

        length = 0

l.append(jeden + dwa)

for iteam in l:
    if iteam != 1 or iteam != 0 :
        score += wzor(iteam)
    elif iteam == 1:
        score += 1

print(int(score))
