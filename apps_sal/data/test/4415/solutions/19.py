n = int(input())
a = list(map(int,input().split()))
f = [0 for i in range(200010)]
inc = []
dec = []
for i in a:
    if f[i]==0:
        inc.append(i)
        f[i]+=1
    elif f[i]==1:
        dec.append(i)
        f[i]+=1
    elif f[i]>1:
        print("NO")
        return
print("YES")
print(len(inc))
print(*(sorted(inc)))
print(len(dec))
print(*(sorted(dec,reverse=True)))
