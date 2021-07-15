n, x = map(int, input().split())
burger = [2 ** (i + 2) - 3 for i in range(n)]
burger2 = [2 ** (i + 1) - 1 for i in range(n)]
num = [0 for i in range(n)]
ans = 0
temp = n - 1
while x > 0:
    if x >= 1:
        x -= 1
    else:
        continue
    if x >= burger[temp]:
        num[temp] += 1
        x -= burger[temp]
    else:
        temp -= 1
        continue
    if x >= 1:
        ans += 1
        x -= 1
    else:
        continue
    if x >= burger[temp]:
        num[temp] += 1
        x -= burger[temp]
    else:
        temp -= 1
        continue
    if x >= 1:
        x -= 1
    else:
        continue
for i in range(n):
    ans += burger2[i] * num[i]
print(ans)
