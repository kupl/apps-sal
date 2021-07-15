n = int(input())
a = list(map(int, input().split()))
b = [0] * n
for i in range(n):
    b[i] = n - a[i]
cnt = [[] for i in range(n + 1)]
for i in range(n):
    cnt[b[i]].append(i)
f = True
for i in range(1, n + 1):
    if len(cnt[i]) % i != 0:
        f = False
        break
if not f:
    print("Impossible")
else:
    t = 1
    ans = [0] * n
    for i in range(1, n + 1):
        x = cnt[i]
        if len(x) != 0:
            y = 0
            for j in x:
                ans[j] = t
                y += 1
                if y == i:
                    t += 1
                    y = 0
    print("Possible")
    print(*ans)
