N,D = map(int,input().split())
area = D*2 + 1
ans = (N+area-1)//area
print(ans)
