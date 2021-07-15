ins = []
sumi = []
ous = []

n = int(input())
l = []
for i in range(n):
    l.append(str(input()))
    sumi.append(0)

sumi.append(0)

for i in range(n):
    if l[i][0] == "+":
        ins.append(l[i][2:len(l[i])])
        for j in range(i+1, n+1):
            sumi[j]+=1
    elif l[i][0] == "-" and l[i][2:len(l[i])] in ins:
        ins.remove(l[i][2:len(l[i])])
        for j in range(i+1, n+1):
            sumi[j]-=1
    else:
        for j in range(0, i+1):
            sumi[j]+=1
            

print(max(sumi))
