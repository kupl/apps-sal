n=int(input())
a=list(map(int,input().split()))
b=[]
cnt=0
for i in range(n):
    if a[i]%2==1:
        print('0')
        return
    else:
        while a[i]%2==0:
            cnt += 1
            a[i] /=  2
        b.append(cnt)
        cnt = 0
print(min(b))
