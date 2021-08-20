import sys


def input():
    return sys.stdin.readline().strip()


n = int(input())
ls = list(map(int, input().split()))
d = [{}]
works = {}
for i in range(n):
    works[i] = True
for i in range(n):
    d.append(dict(d[-1]))
    try:
        d[-1][ls[i]] += 1
        works[i] = False
    except:
        d[-1][ls[i]] = 1
m = n
for l in range(n):
    for r in range(n - 1, l - 1, -1):
        try:
            d[l][ls[r]] += 0
            break
        except:
            d[l][ls[r]] = 1
            pass
    if works[l]:
        m = min(m, r - l + 1)
    else:
        m = min(m, r - l + 1)
        break
if len(set(ls)) == n:
    print(0)
else:
    print(m)
