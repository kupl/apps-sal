l, r = list(map(int, input().split()))
for k in range(l, r+1):
    m = list(str(k))
    h = set(m)
    if len(m) == len(h):
        print(k)
        break
else: print(-1)

