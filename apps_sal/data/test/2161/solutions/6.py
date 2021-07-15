n = int(input())
d = {}
for i in range(n):
    arr = input().split()
    name = arr[0]
    cnt = arr[1]
    arr = arr[2:]
    if name in d:
        for j in arr:
            d[name].append(j)
    else:
        d[name] = arr

print(len(d))
for name in list(d.keys()):
    print(name)
    d[name] = list(set(d[name]))
    ans = []
    for i in range(len(d[name])):
        le = len(d[name][i])
        for j in range(len(d[name])):
            if(i!=j and le < len(d[name][j]) and d[name][j][-le:] == d[name][i]):
                break
        else:
            ans.append(d[name][i])
    ans = set(ans)
    print(len(ans))
    for i in ans:
        print(i)
    

