n, m = [int(v) for v in input().split()]
c = [int(v) for v in input().split()]
a = [int(v) for v in input().split()]

ans = 0

apos = 0
for ci in c:
    if ci <= a[apos]:
        ans += 1
        apos += 1
    if apos >= len(a):
        break

print(ans)

