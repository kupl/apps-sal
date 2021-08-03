import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10**9))
def write(x): return sys.stdout.write(x + "\n")


n = int(input())
s = int(input())


def sub(n, b):
    """nのb進数表記したときの各桁
    n = sum(pow(b,i) * ans[i])
    """
    ans = []
    while n > 0:
        n, v = divmod(n, b)
        ans.append(v)
    return ans


ans = None
for b in range(2, n + 1):
    if b**2 > n:
        break
    if sum(sub(n, b)) == s:
        ans = b
        break
if ans is None:
    ans = float("inf")
    if n == s:
        ans = s + 1
    for p in range(1, n + 1):
        if p**2 > n:
            break
        if (n + p - s) % p == 0:
            b = (n + p - s) // p
            q = s - p
            if b**2 > n and 0 <= q < b and p < b and b * p + q == n and p + q == s:
                ans = min(ans, b)
            else:
                continue
if ans is None or ans == float("inf"):
    ans = -1
print(ans)
