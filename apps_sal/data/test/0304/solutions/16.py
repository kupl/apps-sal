from collections import defaultdict
from copy import deepcopy
a = list(input())
d = defaultdict(int)
for x in a:
    d[int(x)] += 1
fact_mem = {}


def fact(n):
    if n in fact_mem:
        return fact_mem[n]
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    fact_mem[n] = ans
    return ans


mem = {}


def f(d):
    tmp = frozenset(list(d.items()))
    if tmp in mem:
        return 0
    n = sum(d.values())
    ans = 0
    if d[0] > 0:
        ans += (n - d[0]) * fact(n - 1)
    else:
        ans += fact(n)
    if len(d) == 1 and d[0] > 0:
        return 0
    for x in d:
        ans //= fact(d[x])
    for k in d:
        if d[k] > 1:
            e = deepcopy(d)
            e[k] -= 1
            ans += f(e)
    mem[frozenset(list(d.items()))] = ans
    return ans


ans = f(d)
print(ans)
