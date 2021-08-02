n = int(input())
ai = list(map(int, input().split()))
ai.sort()
ans = 0
for i in range(n - 1, -1, -1):
    if ai[-1] - ai[i] > 5:
        break
    ans += 1

num = 0
num2 = 0
while num2 < n:
    if ai[num2] - ai[num] < 6:
        ans = max(ans, num2 - num + 1)
        num2 += 1
    else:
        num += 1
print(ans)
