# In the name of GOD!
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    a[i] -= 1

tk = [0] * n
tm = []
for i in range(n):
    if tk[a[i]] == 0:
        tk[a[i]] = b[i]
    elif tk[a[i]] < b[i]:
        tm.append(tk[a[i]])
        tk[a[i]] = b[i]
    else:
        tm.append(b[i])

ans = cnt = 0
tm.sort()
for i in range(k):
    if tk[i] == 0:
        ans += tm[cnt]
        cnt += 1

print(ans)
