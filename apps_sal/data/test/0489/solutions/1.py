n = int(input())
ai = list(map(int, input().split()))
ai.sort()
i = ai[0]
j = ai[1]
k = ai[2]
ans = 0
for num in range(2, n):
    if k == ai[num]:
        ans += 1
if j == k:
    if i == j:
        num2 = ans
        ans = 0
        for num in range(1, num2 + 2):
            ans += num * (num - 1) // 2
    else:
        ans = ans * (ans + 1) // 2
print(ans)
