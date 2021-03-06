"""
問題：
    文字列 A, B, Cが与えられます。
    これがしりとりになっているか判定してください。

    つまり、
        A の最後の文字と B の最初の文字が同じ
        B の最後の文字と C の最初の文字が同じ
    この 2つが正しいか判定してください。
    両方とも正しいならば YES、そうでないならば NO を出力してください。
"""
'\n制約：\n    A, B, C は全て英小文字(a ~ z)からなる。\n    1 ≦ |A|, |B|, |C| ≦ 10\n    なお、\n    |A|, |B|, |C| は文字列A, B, Cの長さを表します。\n'
(a, b, c) = list(map(str, input().split()))
result = 'ret'
if a[-1] == b[0] and b[-1] == c[0]:
    result = 'YES'
else:
    result = 'NO'
print(result)
