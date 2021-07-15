from collections import Counter
n,c,a=int(input()),Counter(),0
for i in map(int,input().split()):
    a+=sum([c[2**j-i] for j in range(32)])
    c[i]+=1
print(a)

