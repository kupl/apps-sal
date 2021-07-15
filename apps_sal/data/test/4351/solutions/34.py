n = (input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
if n==n[::-1]:
    print('Yes')
else:
    print('No')
