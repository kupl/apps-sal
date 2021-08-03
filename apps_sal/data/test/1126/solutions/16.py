N, X, M = list(map(int, input().split()))

a = X
path = [a]
done = set([a])
while True:
    na = pow(a, 2, M)
    if na in done:
        s = path.index(na)
        break
    else:
        path.append(na)
        done.add(na)
        a = na

if N < s + 1:
    ans = sum(path[:N])
else:
    rest = N - s
    x, y = divmod(rest, len(path) - s)
    ans = sum(path[:s])
    ans += sum(path[s:]) * x
    ans += sum(path[s: s + y])
print(ans)
