n, a, b = list(map(int, input().split()))
t = list(map(int, input().split()))

ans = 0
cnta = 0
cntb1 = 0
cntb2 = 0
for ti in t:
    if ti == 1:
        if cnta < a:
            cnta += 1
        elif cntb1 + cntb2 < b:
            cntb1 += 1
        elif 0 < cntb1:
            cntb1 -= 1
            cntb2 += 1
        else:
            ans += 1
    else:
        if cntb1 + cntb2 < b:
            cntb2 += 1
        else:
            ans += 2
print(ans)
