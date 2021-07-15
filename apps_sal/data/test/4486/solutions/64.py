#072b
#1.値を受け取る
s = str(input())

#2.結果を出力する
for i in range(len(s)):
    if i % 2 == 0:
        print(s[i], end = '')
