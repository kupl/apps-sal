n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = pow(10, 9) + 7
neg = 0
zero = 0
for i in range(n):
    if a[i] >= 0:
        if a[i] == 0:
            zero += 1
        a[i] = [a[i], 1]
    else:
        a[i] = [-a[i], 0]
        neg += 1
a.sort(reverse=True)
ans = 1
if n == k:
    for i in range(n):
        ans *= a[i][0]
        ans %= mod
        if not a[i][1]:
            ans *= -1
            ans %= mod
elif k % 2 == 1 and (neg == n or neg + zero == n):
    for i in range(1, k + 1):
        ans *= -a[-i][0]
        ans %= mod
else:
    pos, neg = 0, 0
    lastpos, lastneg = mod, mod
    for i in range(k):
        ans *= a[i][0]
        ans %= mod
        if a[i][1]:
            pos += 1
            lastpos = a[i][0]
        else:
            neg += 1
            lastneg = a[i][0]
    if neg % 2 == 1:
        firstpos, firstneg = mod, mod
        for i in range(k, n):
            if not firstpos == mod and not firstneg == mod:
                break
            if firstpos == mod and a[i][1]:
                firstpos = a[i][0]
            elif firstneg == mod and not a[i][1]:
                firstneg = a[i][0]
        if not mod in [lastpos, lastneg, firstpos, firstneg]:
            if firstpos * lastpos >= firstneg * lastneg:
                ans = ans * pow(lastneg, mod - 2, mod) * firstpos % mod
            else:
                ans = ans * pow(lastpos, mod - 2, mod) * firstneg % mod
        elif not mod in [lastpos, firstneg]:
            ans = ans * pow(lastpos, mod - 2, mod) * firstneg % mod
        elif not mod in [lastneg, firstpos]:
            ans = ans * pow(lastneg, mod - 2, mod) * firstpos % mod
print(ans)
