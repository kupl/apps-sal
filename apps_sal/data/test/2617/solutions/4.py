n = int(input())
for i in range(int(n)):
    a = int(input())
    
    for j in range(35):
        if a <= 2**j - 1:
            print(j-1)
            break
    l = [2**x for x in range(j)]
    #print(l)
    
    total = sum(l)
    c = 1
    while total != a:
        try:
            l[-c] -= min(l[-c-1], total - a)
            total = sum(l)
            c += 1
            #print(c)
        except:
            pass
    ans = []
    for j in range(len(l) - 1):
        ans.append(l[j+1] - l[j])
    ans = [str(x) for x in ans]
    print(' '.join(ans))
