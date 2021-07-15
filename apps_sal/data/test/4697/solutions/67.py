#n = int(input())
n, m = list(map(int, input().split()))
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

if n >= m//2:
    ans = m//2
else:
    m -= n*2
    ans = n + m//4

print(ans)

