n = int(input())
data = list(map(int,input().split()))
ans = sum(data)
if ans%2==1: 
    print('First')
else:
    for i in data:
        if i%2==1:
            print('First')
            break
    else:
        print('Second')

