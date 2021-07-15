def get_len(a, b):
    if a[0]>=b[0]:
        c = a
        a = b
        b = c
    i = 0
    j = 0
    res = 2
    while i<len(a) and j<len(b):
        while a[i]<=b[j]:
            i+=1
            if i==len(a):
                break
        if i==len(a):
                break
        res+=1
        while a[i]>=b[j]:
            j+=1
            if j==len(b):
                break
        if j==len(b):
                break
        res+=1
    return res


n = int(input())
a = [int(e) for e in input().split()]
d = dict()
keys = []
for i in range(len(a)):
    x = a[i]
    if x in d:
        d[x].append(i)
    else:
        d[x] = [i]
        keys.append(x)
ans = 0
for i in range(len(keys)):
    x = keys[i]
    for j in range(i+1, len(keys)):        
        y = keys[j]
        if x==y:
            continue
        
        i1 = 0
        j1 = 0
        #print("___")
        #print(d[x], d[y])
        xi = get_len(d[x], d[y])        
        #print(xi)
        ans = max(ans, xi)
ans1 = [len(d[e]) for e in d]
ans = max(ans, max(ans1))
print(ans)
# 3 1 3 1 3
        

