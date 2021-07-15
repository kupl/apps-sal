#n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
s = list(input())
if len(s) == len(set(s)):
    print('yes')
else:
    print('no')

