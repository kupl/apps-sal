N = input()
n = len(N)
ans = 0
if n < 3:
    print(0)
    return
if n > 3:
    for i in range(3,n):
        ans += 3**i - 3*(2**i) + 3
a = int(N[0])
if a > 3:
    ans += 3**(n-1) - 2*(2**(n-1)) + 1
if a > 5:
    ans += 3**(n-1) - 2*(2**(n-1)) + 1
if a > 7:
    ans += 3**(n-1) - 2*(2**(n-1)) + 1
b = int(N[1])
c = int(N[2])
if a == 3:
    if b > 3:
        ans += 3**(n-2) - 2*(2**(n-2)) + 1
    if b > 5:
        ans += 3**(n-2) - (2**(n-2))
    if b > 7:
        ans += 3**(n-2) - (2**(n-2))
    if b == 3:
        if c > 3:
            ans += 3**(n-3) - 2*(2**(n-3)) + 1
        if c > 5:
            ans += 3**(n-3) - (2**(n-3))
        if c > 7:
            ans += 3**(n-3) - (2**(n-3))
    if b == 5:
        if c > 3:
            ans += 3**(n-3) - (2**(n-3))
        if c > 5:
            ans += 3**(n-3) - (2**(n-3))
        if c > 7:
            ans += 3**(n-3)
    if b == 7:
        if c > 3:
            ans += 3**(n-3) - (2**(n-3))
        if c > 5:
            ans += 3**(n-3)
        if c > 7:
            ans += 3**(n-3) - (2**(n-3))
elif a == 5:
    if b > 3:
        ans += 3**(n-2) - (2**(n-2))
    if b > 5:
        ans += 3**(n-2) - 2*(2**(n-2)) + 1
    if b > 7:
        ans += 3**(n-2) - (2**(n-2))
    if b == 3:
        if c > 3:
            ans += 3**(n-3) - (2**(n-3))
        if c > 5:
            ans += 3**(n-3) - (2**(n-3))
        if c > 7:
            ans += 3**(n-3)
    if b == 5:
        if c > 3:
            ans += 3**(n-3) - (2**(n-3))
        if c > 5:
            ans += 3**(n-3) - 2*(2**(n-3)) + 1
        if c > 7:
            ans += 3**(n-3) - (2**(n-3))
    if b == 7:
        if c > 3:
            ans += 3**(n-3)
        if c > 5:
            ans += 3**(n-3) - (2**(n-3))
        if c > 7:
            ans += 3**(n-3) - (2**(n-3))
elif a == 7:
    if b > 3:
        ans += 3**(n-2) - (2**(n-2))
    if b > 5:
        ans += 3**(n-2) - (2**(n-2))
    if b > 7:
        ans += 3**(n-2) - 2*(2**(n-2)) + 1
    if b == 3:
        if c > 3:
            ans += 3**(n-3) - (2**(n-3))
        if c > 5:
            ans += 3**(n-3)
        if c > 7:
            ans += 3**(n-3) - (2**(n-3))
    if b == 5:
        if c > 3:
            ans += 3**(n-3)
        if c > 5:
            ans += 3**(n-3) - (2**(n-3))
        if c > 7:
            ans += 3**(n-3) - (2**(n-3))
    if b == 7:
        if c > 3:
            ans += 3**(n-3) - (2**(n-3))
        if c > 5:
            ans += 3**(n-3) - (2**(n-3))
        if c > 7:
            ans += 3**(n-3) - 2*(2**(n-3)) + 1
    
if (a == 3 or a == 5 or a == 7) and (b == 3 or b == 5 or b == 7) and (c == 3 or c == 5 or c == 7):
    d = (a*100 + b * 10 + c) * 10**(n-3)
    e = int(N) + 1
    t = {"3","5","7"}
    for i in range(d,e):
        u = set(str(i))
        if u == t:
            ans += 1
print(ans)
