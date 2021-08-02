n, k = map(int, input().strip().split())
l = list(map(int, input().strip().split()))
test = True
md = 998244353
evens = [0]
odds = [0]
for i in range(n):
    if i % 2:
        odds.append(l[i])
    else:
        evens.append(l[i])
evens.append(-10)
odds.append(-10)
segs = []
l = len(odds)
cont = False
test = True
for i in range(l):
    if odds[i] == -1 and cont == False:
        a = i - 1
        cont = True
    elif odds[i] != -1 and cont == True:
        cont = False
        b = i
        segs.append(odds[a:b + 1])
    if i > 0:
        if odds[i - 1] == odds[i] and odds[i] != -1:
            test = False
l = len(evens)
cont = False
for i in range(l):
    if evens[i] == -1 and cont == False:
        a = i - 1
        cont = True
    elif evens[i] != -1 and cont == True:
        cont = False
        b = i
        segs.append(evens[a:b + 1])
    if i > 0:
        if evens[i - 1] == evens[i] and evens[i] != -1:
            test = False
ans = 1
for seg in segs:
    l = len(seg) - 2
    dp = [[0, 0] for i in range(l)]
    a = seg[-1]
    b = seg[0]
    if b == 0:
        dp[0][0] = 1
        dp[0][1] = k - 1
    elif b == a:
        dp[0][0] = 0
        dp[0][1] = k - 1
    elif b != a:
        dp[0][0] = 1
        dp[0][1] = k - 2
    for i in range(1, l):
        dp[i][0] = (dp[i - 1][1]) % md
        dp[i][1] = (dp[i - 1][0] * (k - 1) + dp[i - 1][1] * (k - 2)) % md
    if a == -10:
        ans *= (dp[l - 1][0] + dp[l - 1][1])
    else:
        ans *= dp[l - 1][1]
    ans %= md
if test == False:
    print(0)
else:
    print(ans)
