n = int(input())
num = list(map(int, input().split()))
mn = min(num)
i = 0
while num[i] != mn:
    i += 1
cur = i
ans = n
for i in range(cur + 1, n):
    if num[i] == mn:
        ans = min(ans, i - cur)
        cur = i
print(ans)
