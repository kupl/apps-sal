n, sl = map(str,input().split())
sl = list(sl)
n = int(n)
atl = [0]
cgl = [0]
at = 0
cg = 0
for s in sl:
    if s == "A":
        at += 1
    elif s == "T":
        at -= 1
    elif s == "C":
        cg += 1
    else:
        cg -= 1
    atl.append(at)
    cgl.append(cg)

ans = 0
for i in range(n+1):
    for j in range(i+1, n+1):
        if atl[j] == atl[i] and cgl[j] == cgl[i]:
            ans += 1

print(ans)
