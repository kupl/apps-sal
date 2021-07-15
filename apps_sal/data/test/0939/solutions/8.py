def readln():
    return tuple(map(int, input().split()))

n, m = readln()
ans = [0] * (n + 1)
for _ in range(m):
    a = readln()
    for i in range(3):
        if ans[a[i]] == 1:
            ans[a[(i + 1) % 3]] = 2
            ans[a[(i + 2) % 3]] = 3
            break
        elif ans[a[i]] == 2:
            ans[a[(i + 1) % 3]] = 1
            ans[a[(i + 2) % 3]] = 3
            break
        elif ans[a[i]] == 3:
            ans[a[(i + 1) % 3]] = 1
            ans[a[(i + 2) % 3]] = 2
            break
    if not ans[a[0]]:
        ans[a[0]] = 1
        ans[a[1]] = 2
        ans[a[2]] = 3
print(' '.join(map(str, ans[1:])))

