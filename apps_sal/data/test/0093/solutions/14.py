def read(s, t):
    if (s[0] == 'X'):
        return s[1] + t[::-1]
    if (s[1] == 'X'):
        return t[::-1] + s[0]
    if (t[0] == 'X'):
        return t[1] + s
    if (t[1] == 'X'):
        return s + t[0]


s1 = ''.join(input().split())
s2 = ''.join(input().split())
t1 = ''.join(input().split())
t2 = ''.join(input().split())
s = read(s1, s2)
t = read(t1, t2)
for i in range(3):
    for j in range(3):
        #print(s[i:] + s[:i], t[j:] + t[:j])
        if s[i:] + s[:i] == t[j:] + t[:j]:
            print("YES")
            return
print("NO")
