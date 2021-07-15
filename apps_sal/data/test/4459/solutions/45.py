N = int(input())
a = [int(s) for s in input().split()]
p = {}

for b in a:
    if b in p:
        p[b] += 1
    else:
        p[b] = 1

ans = 0
for k in p:
    if k > p[k]:
        ans += p[k]
    elif k < p[k]:
        ans += (p[k] - k)

print(ans)
