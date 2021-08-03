

def LI():
    return list(map(int, input().split()))


N, H = LI()
amax = 0
blist = []
for _ in range(N):
    a, b = LI()
    amax = max(amax, a)
    blist.append(b)
blist.sort()
ans = 0
for i in range(N - 1, -1, -1):
    if blist[i] <= amax:
        break
    ans += 1
    H -= blist[i]
    if H <= 0:
        break
if H > 0:
    if H % amax == 0:
        ans += H // amax
    else:
        ans += H // amax + 1

print(ans)
