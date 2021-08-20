n = int(input())
(a1, a2, a3) = list(map(int, input().split()))
(b1, b2, b3) = list(map(int, input().split()))
maxx = min(b2, a1) + min(a2, b3) + min(a3, b1)
c = 0
if b1 > a1:
    c += 1
if b2 > a2:
    c += 1
if b3 > a3:
    c += 1
if c == 1:
    if b1 > a1:
        minn = max(0, min(b1, a3 - (b2 + b3)))
    elif b2 > a2:
        minn = max(0, min(b2, a1 - (b1 + b3)))
    else:
        minn = max(0, min(b3, a2 - (b1 + b2)))
elif a1 > b1:
    minn = max(0, min(b2, a1 - (b1 + b3)))
elif a2 > b2:
    minn = max(0, min(b3, a2 - (b1 + b2)))
else:
    minn = max(0, min(b1, a3 - (b3 + b2)))
print(minn, maxx)
