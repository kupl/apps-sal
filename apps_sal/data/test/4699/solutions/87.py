n,k = map(int,input().split())
d=set(input().split())
while True:
    if len(set(str(n))&d)!=0:
        n+=1
    else:
        break
print(n)
