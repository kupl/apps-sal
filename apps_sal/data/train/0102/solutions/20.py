t = int(input())
for i in range(t):
    n = int(input())
    l = len(str(n))
    ans = (l - 1) * 9
    s = str(n)[0]
    if n >= int(s * l):
        ans += int(s)
    else:
        ans += int(s) - 1
    print(ans)
