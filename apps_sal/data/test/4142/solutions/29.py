# 偶数と奇数配列に分ける
# 奇数番配列にLが存在するかで条件分岐
# 偶数番配列にRが存在するかで条件分岐
S = input()
Odd = S[::2]
Even = S[1::2]
print('Yes' if Odd.count('L') == 0 and Even.count('R') == 0 else 'No')
