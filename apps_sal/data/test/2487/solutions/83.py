n = int(input())
side = 0
for _ in range(n-1):
    u,v = map(int, input().split())
    if v > u:
        side += u*(n-v+1)
    else:
        side += v*(n-u+1)

ans = 0
vertex = 0
for i in range(n):
    vertex += (i+1)*(n-i)

ans= vertex -side
print(ans)
