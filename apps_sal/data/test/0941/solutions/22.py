B,K = list(map(int,input().split()))
A = list(map(int,input().split()))
if B%2==0:
    print('odd' if A[-1]%2 else 'even')
else:
    print('odd' if sum(A)%2 else 'even')

