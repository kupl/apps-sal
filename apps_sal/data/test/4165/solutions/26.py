N = int(input())
L = list(map(int,input().split()))

length = sum(L)-max(L)
if max(L) < length:
    print('Yes')
else:
    print('No') 
