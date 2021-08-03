n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = [0] * m
d = {}
for i in range(n):
    d[a[i]] = i
ans2 = []
a = set(a)
for j in a:
    ans2.append(d[j])
ans2.sort()
ka = [0] * n
c = len(ans2)
for i in range(c):
    ka[ans2[i]] = c - i
i = 0
while i < n and ka[i] == 0:
    i += 1
for j in range(n - 2, -1, -1):
    if ka[j] == 0:
        ka[j] = ka[j + 1]
for i in range(m):
    b = int(input()) - 1
    ans[i] = ka[b]
for i in ans:
    print(i)
