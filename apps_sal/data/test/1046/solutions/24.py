n = int(input())
l = list(map(int, input().split()))
l.sort()
r = 0
bad = False
for i in range(n - 1):
    if l[i] == 0:
        continue
    if l[i] == l[i + 1]:
        r += 1
    if i < n - 2 and l[i + 2] == l[i]:
        print(-1)
        bad = True
        break
if not bad:
    print(r)
