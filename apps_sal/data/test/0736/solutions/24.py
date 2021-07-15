n, m = map(int, input().split())
ans = -1
for i in range((n+1)//2, n+1):
    if i%m==0:
        ans = i
        break
print(ans)
