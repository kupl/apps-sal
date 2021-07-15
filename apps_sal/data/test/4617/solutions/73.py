c1 = input()
c2 = input()

# マス目を 180度回転 させたとき、元のマス目と一致するなら YES を、そうでないなら NO を出力せよ。

if [c1[0], c1[1], c1[2]] == [c2[2], c2[1], c2[0]]:
    print("YES")
else:
    print("NO")
