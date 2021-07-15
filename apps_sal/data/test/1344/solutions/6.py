n = int(input())
ai = list(map(int,input().split()))
num = 1
ans = 0
for i in range(1,n):
    if ai[i] > ai[i-1]:
        num += 1
    else:
        ans = max(num,ans)
        num = 1
ans = max(num,ans)
print(ans)

