# 3個のパックにそれぞれ、a,b,c個のキャンディーが入っている
# キャンディーを2人に分ける際、個数が等しくなるか判定

# 入力
a, b, c = list(map(int, input().split()))

# 処理
if a == b + c or b == a + c or c == a + b:
    print("Yes")
else:
    print("No")

