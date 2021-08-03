n, m = list(map(int, input().split()))
l = list(map(int, input().split()))
a = [0 for _ in range(n)]
f = [False for _ in range(n + 1)]
ans = True
for i in range(m - 1):
    for j in range(1, n + 1):
        if (l[i] + j - 1) % n + 1 == l[i + 1]:
            if a[l[i] - 1] != 0 and a[l[i] - 1] != j:
                ans = False
            else:
                if a[l[i] - 1] == j:
                    break
                if f[j]:
                    ans = False
                f[j] = True
                a[l[i] - 1] = j
            break
j = 1
for i in range(n):
    if not a[i]:
        while j <= n and f[j]:
            j += 1
        a[i] = j
        f[j] = True
if ans:
    print(*a)
else:
    print(-1)
