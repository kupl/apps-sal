# スペース区切りの整数の入力
b, c = map(int, input().split())
 
if b * c % 2 == 0:
  print("Even")
else:
  print("Odd")
