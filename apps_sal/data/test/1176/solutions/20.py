n = int(input())
a = list(map(int, input().split()))

# 全ての値の合計を求め、負の値が偶数個であれば全ての値は非負の値にできる為、合計値を出力
# 負の値の数が奇数個の場合は1つだけが負の値になる為、この場合は最小値を負の値にして合計を出力
ans = 0
count = 0
for i in range(n):
  if a[i] < 0: count += 1 # 負の値をカウント
  a[i] = abs(a[i])
  ans += a[i] # 全ての値を足していく
if count%2 == 0: print(ans) # 負の値が偶数個であればそのまま出力
else:
  ans -= 2*min(a) # 負の値が奇数個であれば最小値の値分減らして出力
  print(ans)
