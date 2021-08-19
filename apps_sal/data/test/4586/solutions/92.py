N = input()

# 3つ以上の同じ数字が連続して並んだ 4桁の整数を 良い整数 とします。
# N が良い整数 ならば Yes を、そうでなければ No を出力せよ。

if N[1] == N[2]:
    if N[0] == N[1] or N[2] == N[3]:
        print("Yes")
    else:
        print("No")
else:
    print("No")
