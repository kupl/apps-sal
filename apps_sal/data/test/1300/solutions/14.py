k=[*map(int,input().split())]
list1=[*map(int,input().split())]
z= [0]*500001
o=0

for i in list1:
    z[i]=max(z[i],z[k[1]])
    z[i]+=1
    o=max(o,z[i]-z[k[1]])
print(o+z[k[1]])
