n, k = [int(x) for x in input().strip().split(" ")]

b = [int(x) for x in input().strip().split(" ")]
c = input().strip()

w = sorted([b[i] for i in range(len(b)) if c[i] == 'W'])
o = sorted([b[i] for i in range(len(b)) if c[i] == 'O'])
r = sorted([b[i] for i in range(len(b)) if c[i] == 'R'])

if k == 1 or len(o) == 0 or len(w) == 0 and len(r) == 0:
    print(-1)
    return

max_wo = -1
if len(w) > 0 and len(w) + len(o) >= k:
    wo = sorted(w[:-1] + o[:-1])
    max_wo = w[-1] + o[-1]
    if k > 2:
         max_wo += sum(wo[-(k-2):])

max_ro = -1
if len(r) > 0 and len(r) + len(o) >= k:
    ro = sorted(r[:-1] + o[:-1])
    max_ro = r[-1] + o[-1]
    if k > 2:
        max_ro += sum(ro[-(k-2):])

ans = max(max_wo, max_ro)
print(ans)

