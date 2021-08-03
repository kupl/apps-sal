import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10**9))
def write(x): return sys.stdout.write(x + "\n")


n, k, q = list(map(int, input().split()))
a = list(map(int, input().split()))
arg = [(num, i) for i, num in enumerate(a)]
arg.sort()


def sub(x):
    """0,1,...,x-1番目は使わない場合において、X-Yの値
    """
    index = [item[1] for item in arg[:x]]
    index.sort()
    index.append(n)
    vals = []
    prv = 0
    for ind in index:
        if ind - prv >= k:
            vals.extend(sorted(a[prv:ind])[:(ind - prv) - k + 1])
        prv = ind + 1
        if prv >= n:
            break
    if len(vals) < q:
        return None
    else:
        vals.sort()
        return vals[q - 1] - arg[x][0]


ans = float("inf")
for i in range(n):
    res = sub(i)
    if res is not None:
        ans = min(ans, res)
print(ans)
