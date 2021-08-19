S = str(input())
T = str(input())

# 英小文字の文字列S を回転させて T に一致させられる場合は Yes、一致させられない場合は No を出力せよ。

for i in range(len(S)):
    if S[i:] + S[:i] == T:
        print("Yes")
        break
else:
    print("No")
