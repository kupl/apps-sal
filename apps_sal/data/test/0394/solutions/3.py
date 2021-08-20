def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


n = ii()
a = [0] + li()
d = [a[i] - a[i - 1] for i in range(1, n + 1)]
ans = []
for i in range(1, n + 1):
    ok = all((d[j] == d[j % i] for j in range(n)))
    if ok:
        ans.append(i)
print(len(ans))
print(*ans)
