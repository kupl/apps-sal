#n = int(input())
w, a, b = list(map(int, input().split()))
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

if a <= b:
    ans = max(0, b-(a+w))
else:
    ans = max(0, a-(b+w))
print(ans)

