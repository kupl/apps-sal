#n = int(input())
x, a, b = list(map(int, input().split()))
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

if a >= b:
    ans = 'delicious'
elif a+x >= b:
    ans = 'safe'
else:
    ans = 'dangerous'
print(ans)

