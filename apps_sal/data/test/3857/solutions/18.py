n = int(input())
a = list(map(int, input().split()))
a.sort()
dp = [0]
for i in a:
    add = False
    for j in range(len(dp)):
        if(dp[j] <= i):
            dp[j] += 1
            add = True
            break
    if not add:
        dp.append(1)
print(len(dp))
