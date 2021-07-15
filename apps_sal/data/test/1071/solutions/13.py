k=sum(map(int,input().split()))
m=sum(map(int,input().split()))
polki=int(input())
kp=(k//5)+1 if k%5 else k//5
mp=(m//10)+1 if m%10 else m//10
if(kp+mp)<=polki:
    print('YES')
else:
    print('NO')
