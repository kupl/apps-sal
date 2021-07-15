from functools import reduce
     
a=int(input())
b=list([int(m) for m in input().split(' ')])

m=max([len(list([m for m in b if m==i])) for i in b]) #количество вхождений

v={a:0 for a in b}

for i in b:
    v[i]+=1
    if v[i]== m:
        print(i)
        return

