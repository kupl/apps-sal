def genrevs(n):
    ans = []
    for l in range(n):
        for r in range(l, n):
            ans.append((l, r))
    return ans

def cnt_rev(p):
    n = len(p)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] > p[j]:
                ans += 1
    return ans

def repl(l, r):
    nonlocal p
    for c in range((r - l + 1) // 2):
        p[l + c], p[r - c] = p[r - c], p[l + c]


n, k = list(map(int, input().split()))
p = list(map(int, input().split()))
rev = genrevs(n)
lr = len(rev)
tr = []
ans = 0
if k == 1:
    for i in range(lr):
        repl(rev[i][0], rev[i][1])
        ans += cnt_rev(p)
        repl(rev[i][0], rev[i][1])
    print(ans / lr)

if k == 2:
    for k1 in range(lr):
        repl(rev[k1][0], rev[k1][1])
        for k2 in range(lr):
            repl(rev[k2][0], rev[k2][1])
            ans += cnt_rev(p)
            repl(rev[k2][0], rev[k2][1])
        repl(rev[k1][0], rev[k1][1])
    print(ans / (lr ** 2))

if k == 3:
    for k1 in range(lr):
        repl(rev[k1][0], rev[k1][1])
        for k2 in range(lr):
            repl(rev[k2][0], rev[k2][1])
            for k3 in range(lr):
                repl(rev[k3][0], rev[k3][1])
                ans += cnt_rev(p)
                repl(rev[k3][0], rev[k3][1])
            repl(rev[k2][0], rev[k2][1])
        repl(rev[k1][0], rev[k1][1])
    print(ans / (lr ** 3))

if k == 4:
    for k1 in range(lr):
        repl(rev[k1][0], rev[k1][1])
        for k2 in range(lr):
            repl(rev[k2][0], rev[k2][1])
            for k3 in range(lr):
                repl(rev[k3][0], rev[k3][1])
                for k4 in range(lr):
                    repl(rev[k4][0], rev[k4][1])
                    ans += cnt_rev(p)
                    repl(rev[k4][0], rev[k4][1])
                repl(rev[k3][0], rev[k3][1])
            repl(rev[k2][0], rev[k2][1])
        repl(rev[k1][0], rev[k1][1])
    print(ans / (lr ** 4))

