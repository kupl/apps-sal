#n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
a = str(input())
b = str(input())
if len(a) < len(b):
    ans = 'LESS'
elif len(a) > len(b):
    ans = 'GREATER'
else:
    n = len(a)
    ans = 'EQUAL'
    for i in range(n):
        if a[i] < b[i]:
            ans = 'LESS'
            break
        elif a[i] > b[i]:
            ans = 'GREATER'
            break
print(ans)
