n, k = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
d = {}
e = []
for i in range(n):
    if a[i] not in d:
        d[a[i]] = [b[i]]
    else:
        d[a[i]].append(b[i])

'''
print(a)
print(b)
print('--------')
print(d)
'''
for i in d:
    if len(d[i]) > 1:
        d[i].pop(d[i].index(max(d[i])))
        e.extend(d[i])
e.sort()
'''
print(d)
print(e)
'''

w = k - len(set(a))
#print(w)

#print(e[0:w])
print(sum(e[0:w]))







