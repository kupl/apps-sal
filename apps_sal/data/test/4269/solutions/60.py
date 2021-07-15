#セキュリティコードは4桁の数字列
#入力しづらい＝連続した箇所がある場合　”Bad＂

S = input()
if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
    print("Bad")
else:
    print("Good")
