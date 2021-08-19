n = int(input())
a = [0] + list(map(int, input().split()))
E = [[] for _ in range(n + 1)]
for i in range(n - 1):
    (p, c) = map(int, input().split())
    E[i + 2] += [(p, c)]
    E[p] += [(i + 2, c)]
ans = 0
ch = [(1, 0, 0)]
while ch:
    (nom, pre, l) = ch.pop()
    if l > a[nom]:
        continue
    ans += 1
    for (x, c) in E[nom]:
        t = l + c if l > 0 else c
        if x != pre:
            ch += [(x, nom, t)]
print(n - ans)
