x,y = map(int,input().split())

lst = [x]
for i in range(10**18):
    if lst[-1]*2 > y:
        break
    else:
        lst.append(lst[-1]*2)

print(len(lst))
