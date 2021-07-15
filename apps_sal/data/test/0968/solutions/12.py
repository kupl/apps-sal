n=int(input())
names=[]
sortnames=[]
result = "YES"
for i in range(n):
    names.append(input().split(' '))
    sortnames.append('')
k = input().split(' ')
for i in range(n):
    k[i] = int(k[i])
    sortnames[i] = names[k[i]-1]
    sortnames[i].sort()
sortnames[0] = sortnames[0][0]
for i in range(n-1):
    if sortnames[i] < sortnames[i+1][0]:
        sortnames[i+1] = sortnames[i+1][0]
    else:
        if sortnames[i] < sortnames[i+1][1]:
            sortnames[i+1] = sortnames[i+1][1]
        else:
            result = "NO"
            break
print(result)

