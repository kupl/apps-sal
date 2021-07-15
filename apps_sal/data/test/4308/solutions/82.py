#n = int(input())
n,k = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

ans=0 if n % k== 0 else 1

print(ans)
