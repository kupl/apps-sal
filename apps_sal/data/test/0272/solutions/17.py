s = input()
s1 = input()
q = set()
z = set()
flag = 0
for i in range(len(s)):
    if(s[i] != s1[i] and (s1[i], s[i]) not in q and (s[i], s1[i])not in q):
        q.add((s[i], s1[i]))
        if(s[i] in z or s1[i] in z):
            flag = 1
        z.add(s[i])
        z.add(s1[i])
for i in range(len(s)):
    if(s[i] == s1[i] and s[i] in z):
        flag = 1
if(flag):
    print(-1)
else:
    print(len(q))
    for item in q:
        print(item[0], item[1])
