#n = int(input())
a, b = list(map(int, input().split()))
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
ans = a + b
if a + b >= 10:
    ans = 'error'
print(ans)
