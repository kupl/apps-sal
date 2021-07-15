# キャンディの個数を取得
a,b,c = map(int,input().split())

#判定結果をもとにメッセージを出力
if a == b + c\
or b == a + c\
or c == a + b:
  print("Yes")
else:
  print("No")
