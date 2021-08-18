n, m = map(int, input().split())
s, t = input(), input()
if '*' not in s:
    if s == t:
        print("YES")
    else:
        print("NO")
    return
s1 = s[:s.find('*')]
s2 = s[s.find('*') + 1:]
if t[:len(s1)] == s1 and t[len(t) - len(s2):] == s2 and len(s1) + len(s2) <= len(t):
    print("YES")
else:
    print("NO")
