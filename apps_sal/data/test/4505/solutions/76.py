S = str(input())

# S を abc を並び替えて作ることができるなら Yes を、そうでないなら No を出力せよ。

abc = [S[0], S[1], S[2]]
if "a" in abc and "b" in abc and "c" in abc:
    print("Yes")
else:
    print("No")
