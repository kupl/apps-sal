(a, b, w, x, c) = list(map(int, input().split()))
ans = 0
bb = b
benefit = 0
Visited = [False] * 1003
CycleCost = -1
while 1:
    if c <= a:
        break
    if Visited[b] != False:
        CycleCost = ans - Visited[b][1]
        CycleBenefit = benefit - Visited[b][0]
        CycleBegining = b
        break
    Visited[b] = (benefit, ans)
    if b < x:
        b = w - (x - b)
        ans += 1
    elif b >= x:
        b -= x
        ans += 1
        benefit += 1
    if benefit == c - a:
        break
if CycleCost == -1:
    print(ans)
else:
    c -= benefit
    diff = c - a
    xx = diff // CycleBenefit
    if xx != 0:
        xx -= 1
        ans += xx * CycleCost
        diff -= xx * CycleBenefit
    b = CycleBegining
    while diff > 0:
        if b < x:
            b = w - (x - b)
            ans += 1
        else:
            b -= x
            ans += 1
            diff -= 1
    print(ans)
