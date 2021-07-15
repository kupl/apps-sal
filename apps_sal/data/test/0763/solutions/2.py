n = int(input())
num = list(map(int, input().split()))
ans = 10 ** 18
for x in range(1, n + 1):
    res = 0
    for i in range(1, n + 1):
        res += (abs(x - i) + abs(i - 1) + abs(x - 1)) * num[i - 1]
    for i in range(1, n + 1):
        res += (abs(x - 1) + abs(i - 1) + abs(x - i)) * num[i - 1]
    ans = min(res, ans)
print(ans)
