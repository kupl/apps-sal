"""input
5 3
2 6
3 6
2 5
3 5
1 11
"""
(n, m) = map(int, input().split())
a = [None] * n
s = [0] * (max(n, m) + 1)
cnt = [0] * (max(n, m) + 1)
ans = [0] * (max(n, m) + 1)
for i in range(n):
    (x, y) = map(int, input().split())
    a[i] = (x - 1, y)
a = sorted(a, key=lambda x: x[1], reverse=True)
for i in range(n):
    cnt[a[i][0]] += 1
    s[a[i][0]] += a[i][1]
    ans[cnt[a[i][0]]] += max(0, s[a[i][0]])
print(max(ans))
