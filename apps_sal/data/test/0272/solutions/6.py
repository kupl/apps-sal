s1 = input()
s2 = input()

d = {}
d2 = {}

flag = False

for i in range(len(s1)):
    if s1[i] in d:
        if d[s1[i]] != s2[i]:
            flag = True
            break

    if s2[i] in d:
        if d[s2[i]] != s1[i]:
            flag = True
            break
    else:
        d[s1[i]] = s2[i]
        d[s2[i]] = s1[i]
        if s1[i] != s2[i]:
            d2[s1[i]] = s2[i]

if flag:
    print(-1)
else:
    l = len(d2)
    if not l:
        print(0)
    else:
        print(l)
        for item in d2:
            print(item, d2[item])
            
            

