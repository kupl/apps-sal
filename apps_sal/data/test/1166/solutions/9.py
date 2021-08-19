n = int(input())
a = [int(s) for s in input().split()]
ans = [None] * n


def get(p):
    if ans[p] is not None:
        return ans[p]
    elif a[p] == 1:
        ans[p] = 'A'
    elif a[p] == n:
        ans[p] = 'B'
    else:
        for i in range(p + a[p], n, a[p]):
            if a[i] > a[p]:
                if get(i) == 'B':
                    ans[p] = 'A'
                    return ans[p]
        for i in range(p - a[p], -1, -a[p]):
            if a[i] > a[p]:
                if get(i) == 'B':
                    ans[p] = 'A'
                    return ans[p]
        ans[p] = 'B'
    return ans[p]


if n == 1:
    print('B')
else:
    for i in range(n - 1, -1, -1):
        get(i)
    print(''.join(ans))
