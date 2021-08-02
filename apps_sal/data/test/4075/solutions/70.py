def f(i):
    if i == n:
        on = [0] * m
        for j in range(m):
            for k in range(1, s[j][0] + 1):
                if t[s[j][k] - 1]:
                    on[j] += 1
        for j in range(m):
            if not on[j] % 2 == p[j]:
                return
        nonlocal ans
        ans += 1
        return
    t[i] = 1
    f(i + 1)
    t[i] = 0
    f(i + 1)
    return


n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))
ans = 0
t = [0] * n
f(0)
print(ans)
