n, k = map(int, input().split())
a = list(map(int, input().split()))
m = sum(a)
cd = set(())
for i in range(1, int(m**0.5) + 2):
    if m % i == 0:
        cd.add(i)
        cd.add(m // i)
cd = list(cd)
cd.sort(reverse=True)


def func(x):
    r = [ai % x for ai in a]
    r.sort()
    tmp = 0
    sr = [0]
    for ri in r:
        tmp += ri
        sr.append(tmp)
    for i in range(n + 1):
        tmp0 = sr[i]
        tmp1 = (n - i) * x - (sr[-1] - sr[i])
        if tmp0 == tmp1 and tmp0 <= k:
            return True
    return False


for x in cd:
    if x == 1:
        print(1)
        return
    if func(x):
        print(x)
        return
