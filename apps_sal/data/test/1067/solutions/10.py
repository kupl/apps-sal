def mi():
    return list(map(int, input().split()))


'\n5\n-5 -3 5 3 0\n'
n = int(input())
a = sorted(list(mi()))
ans = 0
skip = False
for i in range(n):
    if skip:
        skip = False
        continue
    if i < n - 1:
        if abs(-1 - a[i]) + abs(-1 - a[i + 1]) <= abs(1 - a[i]) + abs(1 - a[i + 1]):
            ans += abs(-1 - a[i]) + abs(-1 - a[i + 1])
        else:
            ans += abs(1 - a[i]) + abs(1 - a[i + 1])
        skip = True
    else:
        ans += abs(1 - a[i])
print(ans)
