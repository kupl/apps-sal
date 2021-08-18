n = int(input())
l = []
for i in range(n):
    s = str(input())
    l.append([len(s), s])
l.sort()
#print( l )
for i in range(n - 1):
    if l[i][1] not in l[i + 1][1]:
        print("NO")
        return
print("YES")
for i in range(n):
    print(l[i][1])
