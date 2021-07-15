n = int(input())
ai = list(map(int,input().split()))
ai.sort()
num = n
ans = 0
for i in ai:
    num -= 1
    ans += 1
    ans = min(i,ans)
print(ans+1)

