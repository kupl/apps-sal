n, m = map(int, input().split())

a = []

for i in range(n):
    l, r = map(int, input().split())
    a.append((l, 0))
    a.append((r, 1))

a.sort()

ok = True
first = True
cnt = 0
for ev in a:
    if first:
        first = False
        if ev[0] != 0:
            ok = False
            break
    if ev[1] == 0:
        cnt += 1
    else:
        cnt -= 1
        if cnt == 0 and ev[0] != m:
            ok = False
    

print("YES" if ok else "NO")
