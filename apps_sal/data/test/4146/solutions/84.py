from collections import Counter
N=int(input())
v=list(map(int,input().split()))

list_odd=v[1::2]
list_even=v[0::2]

cnt_odd=Counter(list_odd)
cnt_even=Counter(list_even)

cnt_odd_sorted=sorted(cnt_odd.items(),reverse=True,key=lambda x:x[1])
cnt_even_sorted=sorted(cnt_even.items(),reverse=True,key=lambda x:x[1])

if cnt_odd_sorted[0][0]!=cnt_even_sorted[0][0]:
    ans=len(list_odd)-cnt_odd_sorted[0][1]
    ans+=len(list_even)-cnt_even_sorted[0][1]

else:
    if len(cnt_odd)==1 and len(cnt_even)==1:
        ans=len(list_even)
    elif len(cnt_odd)==1:
        ans=len(list_even)-cnt_even_sorted[1][1]
    elif len(cnt_even)==1:
        ans=len(list_odd)-cnt_odd_sorted[1][1]
    else:
        ans1=len(list_even)-cnt_even_sorted[1][1]
        ans1+=len(list_odd)-cnt_odd_sorted[0][1]

        ans2=len(list_odd)-cnt_odd_sorted[1][1]
        ans2+=len(list_even)-cnt_even_sorted[0][1]
        ans=min(ans1,ans2)

print(ans)
