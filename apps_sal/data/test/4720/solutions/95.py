n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
ans = 0
for i in range(n):
    l, r = list(map(int, input().split()))
    ans += r - l + 1
print(ans)
