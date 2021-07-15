K=int(input())
A,B=list(map(int, input().split()))

s=0
for i in range(A,B+1):
    if i%K==0:
        print('OK')
        s=s+1
        break

if s==0:
    print('NG')    

