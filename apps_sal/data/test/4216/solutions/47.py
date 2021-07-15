n=int(input())

root=int(n**0.5)

min_keta=10000000000
for i in range(1,root+1):
    if n%i==0:
        one=len(str(i))
        two=len(str(n//i))
        min_keta=min(min_keta,max(one,two))




print(min_keta)

