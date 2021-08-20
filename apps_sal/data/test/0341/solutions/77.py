(n, k) = map(int, input().split())
(r, s, p) = map(int, input().split())
t = list(input())
l = [0] * n
for i in range(n):
    if t[i] == 'r':
        l[i] = p
    elif t[i] == 's':
        l[i] = r
    else:
        l[i] = s
ans = sum(l)
for i in range(k, n):
    if t[i] == t[i - k]:
        ans -= l[i]
        t[i] = 'o'
print(ans)
