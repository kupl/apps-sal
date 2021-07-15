kheap=int(input())
heaps=list(map(int,input().split()))
kworms=int(input())
worms=list(map(int,input().split()))
d1={i:0 for i in range(1,sum(heaps)+1)}
prev=0
counter=1
for i in heaps:
    start=prev+1
    prev+=i
    for i2 in range(start,prev+1):
        d1[i2]=counter
    counter+=1
for num in worms:
    print(d1[num])
