n=int(input())
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
dic={}
arr=0
maxim=0
for i in range(n):
    dic[b[i]]=i
for item in a:
    if dic[item]<maxim:
        arr+=1
    maxim=max(maxim,dic[item])
print(arr)
    

