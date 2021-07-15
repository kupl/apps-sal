R = lambda: list(map(int, input().split()))


def dfs(a):
    cnt = 0
    n = len(a)
    a.append(10000000)
    for i in range(1, n):
        if a[i] != a[i - 1]:
            cnt = 0
        else:
            cnt += 1
        if cnt >= 2:
            j = i
            while a[j] == a[i]:
                j += 1

            return j - i + 2 + dfs(a[:i - 2] + a[j:n])
    return 0


n, k, x = R()
a = R()
ans=1
for i in range(n+1):
    ans=max(ans, dfs(a[:i]+[x]+a[i:]))

print(ans-1)
