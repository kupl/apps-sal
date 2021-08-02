n, m = [int(x) for x in input().split()]

best = 0
ans = []


def foo(p):
    ans = 0
    for i in range(n):
        for j in range(i, n):
            ans += min(p[i:j + 1])
    return ans


def eval(p):
    nonlocal ans, best
    val = foo(p)
    if val > best:
        ans = [p]
        best = val
    elif val == best:
        ans.append(p)


def generate(l=[], remaining=list(range(1, n + 1))):
    if not remaining:
        eval(l)
    else:
        for i, x in enumerate(remaining):
            generate(l + [x], remaining[:i] + remaining[i + 1:])


generate()
print(' '.join(str(x) for x in ans[m - 1]))
