# スペース区切りの整数の入力
a, b, c = input().split()
number = int(a + b + c)
if number % 4 == 0:
  print("YES")
else:
  print("NO")
