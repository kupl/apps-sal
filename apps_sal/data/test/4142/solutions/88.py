# Sの各文字は L, R, U, D のいずれか
S = input()

odd_step = list(S[0::2])
even_step = list(S[1::2])

# UとDはodd,evenともに被っている
# oddとevenの判別はRとLだけ

# not in演算子で入っていないことを確認
if 'R' not in even_step and 'L' not in odd_step:
    print('Yes')
else:
    print('No')

