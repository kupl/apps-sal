n = int(input())
'①\u30001 + 2 + 3 + ・・・+ k <= n + 1\u3000を満たす最大のkを求める。\n\u3000 ②\u3000n - k + 1が答え\n'
'二分探索法を用いてkを求める'
left = 0
right = n + 1
while right - left > 1:
    mid = left + (right - left) // 2
    flag = True
    if (1 + mid) * mid // 2 <= n + 1:
        flag = True
    else:
        flag = False
    if flag:
        left = mid
    else:
        right = mid
print(n - left + 1)
