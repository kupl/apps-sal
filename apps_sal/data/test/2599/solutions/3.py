def f(x):
    return sum(map(int, str(x)))

def subsolve(n, k, x):
    x = max(0, x - 20)
    ans = -1
    for _ in range(41):
        s = 0
        for i in range(k + 1):
            s += f(x + i)
        if s == n:
            ans = x
            break
        x += 1
    return ans

def solve():
    n, k = map(int, input().split())
    u = k * (k + 1) // 2
    if n < u:
        print(-1)
        return
    m = (n - u) // (k + 1)
    x = []
    while m:
        w = min(m, 9)
        x.append(str(w))
        m -= w
    x.reverse()
    if not x:
        print(subsolve(n, k, 0))
        return
    xl = len(x)
    tl = 10 ** (xl - 1)
    first = int(x[0])
    x = int(''.join(x))
    ans = -1
    for j in range(3):
        tj = 10 ** j
        for i in range(10):
            w = subsolve(n, k, (x + (i - first) * tl) * tj)
            if ans == -1 or w != -1 and w < ans:
                ans = w
    print(ans)

t = int(input())
for _ in range(t):
    solve()
