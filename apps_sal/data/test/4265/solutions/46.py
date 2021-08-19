s = input()
t = input()
if s == t:
    print(0)
else:
    p = -1
    ans = 0
    for i in s:
        p += 1
        if i != t[p]:
            ans += 1
    print(ans)
