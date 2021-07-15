n,f = input().split()
n = int(n)
f = int(f)
a = []
for i in range(n):
    x,y = input().split()
    a.append((int(x),int(y)))

a = sorted(a)
s = a[0][1]
mx = s
k = 0
for i in range(1,len(a)):
    if a[i][0] - a[k][0] < f:
        s = s + a[i][1]
    else:
        s = s - a[k][1] + a[i][1]
        for j in range(k+1,i+1):
            if a[i][0] - a[j][0]<f:
                s = s
                k = j
                break
            else:
                s = s - a[j][1]
                k = j
    
    if s>mx:
        mx = s

print (mx)








