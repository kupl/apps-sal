A, B, C = map(str, input().split())

# 文字列 A,B,Cが与えられます。これがしりとりになっているか判定してください。
# 正しいならば YES、そうでないならば NO を出力してください。

if A[-1] == B[0] and B[-1] == C[0]:
    print("YES")
else:
    print("NO")
