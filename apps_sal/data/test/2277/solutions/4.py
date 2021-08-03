n = int(input())
a = list(map(int, input().split()))
pf = [0]
for i in range(n):
    k = a[i]
    inv = 0
    for j in range(i):
        if a[j] > a[i]:
            inv += 1
    pf.append(inv + pf[-1])
ans = pf[-1] % 2
asss = []
m = int(input())
cs = [(i * (i - 1) // 2) % 2 for i in range(1501)]
for _ in range(m):
    l, r = list(map(int, input().split()))
    c = r - l + 1
    if c > 1 and cs[c] == 1:
        ans += 1
        ans %= 2
    if ans:
        asss.append('odd')
    else:
        asss.append('even')
for i in asss:
    print(i)
