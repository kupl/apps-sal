n = int(input())
ai = list(map(int,input().split()))
num = 0
ans = 0
for i in range(n):
    num = max(num,ai[i] - 1)
    if num == i:
        ans += 1
print(ans)

