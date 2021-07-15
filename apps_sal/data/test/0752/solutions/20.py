n = int(input())
a = {}
b = {}
for i in range(n):
    temp = input()
    if temp in a:
        a[temp]+=1
    else: a[temp] = 1
for i in range(n):
    temp = input()
    if temp in b:
        b[temp]+=1
    else: b[temp] = 1
counter = 0
for i in b.keys():
    if i in a:
        if b[i] > a[i]:
            b[i] -= a[i]
        else: b[i] = 0
    counter += b[i]
print(counter)
