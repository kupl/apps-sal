n=int(input())

a_raw=list(map(int,input().split()))
a=[0]*100001
for a_i in a_raw:
    a[a_i]+=1
q=int(input())
sum_tmp=sum(a_raw)

for _ in range(q):
    b,c=list(map(int,input().split()))
    sum_tmp = sum_tmp + c*a[b]-b*a[b]
    a[c]+=a[b]
    a[b]=0
    print(sum_tmp)

