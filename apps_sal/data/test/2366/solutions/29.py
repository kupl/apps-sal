n = int(input())
al = list(map(int, input().split()))

ll = [0 for _ in range(n)]
fl = []
tl = []

for a in al:
    ll[a-1] += 1

for l in ll:
    if l >= 2:
        fl.append(l*(l-1)//2)
        tl.append((l-1)*(l-2)//2)
    else:
        fl.append(0)
        tl.append(0)
cnt = sum(fl)
for a in al:
    print((cnt-fl[a-1]+tl[a-1]))

