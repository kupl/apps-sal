N, T = list(map(int, input().split()))

ans = 0
curM = None
for n in range(N):
    s, d = list(map(int, input().split()))
    if T <= s or (T - s) % d == 0:
        s = s
    else:
        incre = ((T - s) // d + 1) * d
        s += incre
    if curM == None:
        curM = s

    else:
        if curM > s:
            ans = n
            curM = s
print(ans + 1)
