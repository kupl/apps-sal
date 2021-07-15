n = int(input())
ai = list(map(int,input().split()))
ans = 0
for i in range(n):
    if ai[i] == 2:
        ans += 1
print(min(n - ans,ans)+max(0,(n-ans*2)//3))

