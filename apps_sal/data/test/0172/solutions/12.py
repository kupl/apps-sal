n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if (a.count(1)+b.count(1))%2!=0 or (a.count(2)+b.count(2))%2!=0 or (a.count(3)+b.count(3))%2!=0 or (a.count(4)+b.count(4))%2!=0 or (a.count(5)+b.count(5))%2!=0:
    print(-1)
else:
    k=0
    k+=abs(a.count(1)-b.count(1))//2
    k+=abs(a.count(2)-b.count(2))//2
    k+=abs(a.count(3)-b.count(3))//2
    k+=abs(a.count(4)-b.count(4))//2
    k+=abs(a.count(5)-b.count(5))//2
    print(k//2)
