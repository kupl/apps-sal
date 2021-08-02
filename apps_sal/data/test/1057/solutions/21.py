n = int(input())
s = input()

mod = 998244353

left = s[0]
right = s[-1]

ans = 1  # include remove all

if left != right:
    lcount = 0
    for i in range(n):
        if s[i] == left:
            lcount += 1
        else:
            break
    rcount = 0
    for i in reversed(range(n)):
        if s[i] == right:
            rcount += 1
        else:
            break
    ans += lcount + rcount
    print(ans % mod)
else:
    lcount = 0
    for i in range(n):
        if s[i] == left:
            lcount += 1
        else:
            break
    rcount = 0
    for i in reversed(range(n)):
        if s[i] == right:
            rcount += 1
        else:
            break
    if lcount == len(s):
        print((n * (n - 1) // 2 + n) % mod)
    else:
        print((rcount + 1) * (lcount + 1) % mod)
