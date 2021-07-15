def mi():
    return list(map(int, input().split()))
'''
'''
n,k = mi()
a = list(mi())
b = set(a)
t = [[] for i in range(5004)]
for i in range(n):
    t[a[i]].append(i)
c = [0]*n
col = 1
for i in range(5004):
    if len(t[i])>k:
        print ('NO')
        return
    for j in range(len(t[i])):
        c[t[i][j]] = col
        col+=1
        if col==k+1:
            col = 1
if len(set(c))<k:
    print ('NO')
    return
print('YES')
print(*c)

