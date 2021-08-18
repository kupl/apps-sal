import math

A, B, n = map(int, input().split())
lCurKarafs = 0
lSum = 0
aa = 0
bb = 0
c = 0
D = 0
sol = 0
tth = 0
while(n > 0):
    l, t, m = map(int, input().split())
    lCurKarafs = A + (l - 1) * B
    lSum = m * t
    if(lCurKarafs > t):
        print(-1)
    elif(lCurKarafs == t):
        print(l)
    else:
        tth = (t - lCurKarafs + B) // B
        aa = B
        bb = 2 * lCurKarafs - B
        c = (-2) * lSum
        D = bb * bb - 4 * aa * c
        sol = int((math.sqrt(D) - bb) / (2 * aa))
        sol = min(tth, sol)
        sol = l + sol - 1
        print(sol)
    n -= 1
