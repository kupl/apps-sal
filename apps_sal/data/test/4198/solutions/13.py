a, b, x = [int(i) for i in input().split()]
left = 0
right = 10 ** 9 + 1
while right - left > 1:
  mid = (right + left) // 2
  if mid * a + b * len(str(mid)) > x:
    right = mid
  else:
    left = mid
print(left)
