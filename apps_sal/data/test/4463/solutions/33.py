#n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
s = list(input())
t = list(input())
s.sort()
t.sort(reverse=True)
if s < t:
    print('Yes')
else:
    print('No')

