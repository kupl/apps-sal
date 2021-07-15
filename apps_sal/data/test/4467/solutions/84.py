N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
cd = [list(map(int, input().split())) for _ in range(N)]
ab.sort(reverse=True)
cd.sort()
p = 0
for c in cd:
    ac = [-1, -1]
    for a in ab:
        if c[0] > a[0] and c[1] > a[1] and ac[1] < a[1]:
            ac = a
    if ac != [-1, -1]:
        p += 1
        ab.remove(ac)

print(p)
