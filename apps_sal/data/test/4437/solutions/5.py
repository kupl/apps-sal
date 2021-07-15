n=int(input())
a=input()
res=0
res2=''
for i in range (0,len(a),2):
    if a[i]==a[i+1]:
        res+=1
        res2+='ab'
    else:
        res2+=a[i]
        res2+=a[i+1]
print(res)
print(res2)
