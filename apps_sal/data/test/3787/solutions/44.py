import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10**9))
def write(x): return sys.stdout.write(x + "\n")


n, a, b = map(int, input().split())


def sub(n, a, b):
    ps = list(range(a))
    for i in range(1, b):
        ps.append(-a * i)
    count = a + b - 1
    if count == n:
        return ps
    for i in range(1, b):
        for j in range(1, a):
            ps.append(-a * i + j)
            count += 1
            if count == n:
                break
        if count == n:
            break
    return ps


if a + b > n + 1:
    ans = -1
elif a * b < n:
    ans = -1
else:
    # a*b個の列
    ps = sub(n, a, b)
    pps = [(i + 1, p) for i, p in enumerate(ps)]
    pps.sort(key=lambda x: x[1])
    ans = [item[0] for item in pps]
if ans == -1:
    print(ans)
else:
    write(" ".join(map(str, ans)))
