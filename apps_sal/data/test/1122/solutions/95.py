N,M=map(int,input().split())
sets=[]
if N%2==1:
    for i in range(M):
        sets.append((i+1,i+1+(N-3-2*i)+1))
elif N%2==0:
    count=0
    kukan=[]
    for i in range(N//2-1):
        kukan.append(count)
        count+=2
        if count==N//2 or count==N//2-1:
            count+=1
    kukan.reverse()
    for i in range(M):
        sets.append((i+1,i+1+kukan[i]+1))
for set1 in sets:
    print(set1[0],set1[1])
