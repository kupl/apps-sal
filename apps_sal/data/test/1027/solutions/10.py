def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


a = li()
ans = 0
for i in range(14):
    if a[i] == 0:
        continue
    q = a[i] // 14
    r = a[i] % 14
    b = [x + q for x in a]
    b[i] = q
    for j in range(r):
        b[(i + 1 + j) % 14] += 1
    ans = max(ans, sum((x for x in b if x % 2 == 0)))
print(ans)
