
n, p = list(map(int, input().split()))
arr = [input() for _ in range(n)]
arr.reverse()

money = 0
apples = 0
for line in arr:
    if line == 'halfplus':
        money += apples * 2 + 1
        apples = apples * 2 + 1
    else:
        money += apples * 2
        apples = apples * 2

print(money * p // 2)
