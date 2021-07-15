n, k = map(int, input().split())
names = []

def getNext(a):
    if a[1] == 'z':
        return chr(ord(a[0]) + 1) + 'a'
    else:
        return a[0] + chr(ord(a[1]) + 1)

a = list(input().split())
for i in range(len(a)):
    a[i] = 1 if a[i] == 'YES' else 0

tmp = 'Aa'
names.append(tmp)
if a[0]:
    for i in range(k - 1):
        tmp = getNext(tmp)
        names.append(tmp)
else:
    names.append(tmp)
    for i in range(k - 2):
        tmp = getNext(tmp)
        names.append(getNext(tmp))  
        
for i in range(k, n):
    if a[i - k + 1]:
        tmp = getNext(tmp)
        names.append(getNext(tmp))
    else:
        names.append(names[i - k + 1])
print(*names)
