n = int(input())
t = list(map(int, input().split()))
m = int(input())
px = []
for _ in range(m):
    p, x = map(int, input().split())
    px.append((p - 1, x))
for i in range(m):
    ans = 0
    p, x = px[i]
    for j in range(n):
        if j == p:
            ans += x
        else:
            ans += t[j]
    print(ans)
