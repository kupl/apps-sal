n=int(input())
D=list(map(int,input().split()))

count=1
ANS=0

for i in range(1,n):
    if D[i]<=2*D[i-1]:
        count+=1
    else:
        if ANS<count:
            ANS=count
        count=1

if ANS<count:
    ANS=count

    #print(i,count,ANS)

print(ANS)

