a = list(map(str, input().replace(';', ',').split(',')))
#print(a)
c = []
d = []
for i in a:
    try:
        if str(int(i)) == i:
            c += [i]
        else:
            d += [i]
    except:
        d += [i]
if len(c) == 0:
    print("-")
else:
    ans = ""
    for i in c:
        ans += i + ','
    print('"' + ans[:-1] + '"')
if len(d) == 0:
    print("-")
else:
    ans = ""
    for i in d:
        ans += i + ','
    print('"' + ans[:-1] + '"')
    
    

