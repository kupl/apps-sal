n = int(input())
d = {}
for i in range(n):
    s = [z for z in input().split()]
    name = s[0]
    count = int(s[1])
    for z in range(count):
        if name in d.keys():
            d[name].append(s[2 + z])
        else:
            d[name] = [s[2 + z]]
            
for k in d.keys():
    a = set(d[k])
    a = list(a)
    b = []
    for i in range(len(a)):
        f = False
        for j in range(len(a)):
            if i != j:
                if len(a[i]) <= len(a[j]):
                    if a[j][len(a[j]) - len(a[i]):] == a[i]:
                        f = True
                        break
        if f == False:
            b.append(a[i])
    d[k] = b
print(len(d))
for k in d.keys():
    print(k, end = ' ')
    print(len(d[k]), end = ' ')
    print(' '.join(d[k]))
                
            
    
