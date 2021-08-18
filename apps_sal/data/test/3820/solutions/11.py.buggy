n = input()
s = input()
t = input()
p = s.find('*')
if (p == -1):
    if (s == t):
        print("YES")
    else:
        print("NO")
    return
sl = len(s) - p - 1
if (s[:p] == t[:p] and t[len(t) - sl:] == s[p + 1:] and len(t) >= len(s) - 1):
    print("YES")
else:
    print("NO")
