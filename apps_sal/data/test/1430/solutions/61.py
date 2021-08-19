(n, k) = list(map(int, input().split()))
s = input()
on = []
off = []
acnt = 0
bcnt = 0
for i in s:
    if i == '0':
        if bcnt > 0:
            off.append(bcnt)
            bcnt = 0
        acnt += 1
    else:
        if acnt > 0:
            on.append(acnt)
            acnt = 0
        bcnt += 1
if bcnt > 0:
    off.append(bcnt)
    bcnt = 0
if acnt > 0:
    on.append(acnt)
    acnt = 0
ans = 0
if s[0] == '1':
    for i in range(len(on) - k + 1):
        s = 0
        if i == 0:
            a = sum(on[i:i + k])
            b = sum(off[i:i + k + 1])
        else:
            a += on[i + k - 1]
            a -= on[i - 1]
            if i + k <= len(off) - 1:
                b += off[i + k]
            b -= off[i - 1]
        s = a + b
        ans = max(ans, s)
else:
    for i in range(len(on) - k + 1):
        if i == 0:
            a = sum(on[i:i + k])
            b = sum(off[i:i + k])
        elif i == 1:
            a = sum(on[i:i + k])
            b = sum(off[i - 1:i + k])
        else:
            a += on[i + k - 1]
            a -= on[i - 1]
            if i + k - 1 <= len(off) - 1:
                b += off[i + k - 1]
            b -= off[i - 2]
        s = a + b
        ans = max(ans, s)
if ans == 0:
    print(n)
else:
    print(ans)
