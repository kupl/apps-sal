#1
n = int(input())
a = []
b = []
d = 0
for i in range(n):
    a.append(input())
for i in range(n):
    b.append(input())
for i in range(n):
    if(not(a[i] in b)):
        d+=1
    else:
        for j in range(n):
            if(b[j] == a[i]):
                b.remove(b[j])
                break
print(d)

