n = int(input())
A = list(map(int, input().split()))
dp = [[-9999999999, -9999999999]]
for elem in A:
    dp += [[0, 0]]
    if elem % 2 == 0:
        dp[-1][0] = max(dp[-2][0] + elem, dp[-2][0], elem)
        dp[-1][1] = max(dp[-2][1] + elem, dp[-2][1])
    else:
        dp[-1][0] = max(dp[-2][1] + elem, dp[-2][0])
        dp[-1][1] = max(dp[-2][0] + elem, dp[-2][1], elem)
print(dp[-1][1])
