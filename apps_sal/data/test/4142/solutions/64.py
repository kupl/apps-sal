step = input()

# 条件：
# 奇数文字目がすべて R, U, D のいずれか。偶数文字目がすべて L, U, D のいずれか。
# S が「踏みやすい」文字列なら Yes を、そうでなければ No を出力してください。

s = list(step)

odd_list = s[0::2]
even_list = s[1::2]

if 'L' in odd_list or 'R' in even_list:
    print('No')
else:
    print('Yes')
