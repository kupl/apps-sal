# 入力
N = int(input())

# 処理&出力
if N < 1000:
    print('ABC')
elif 1000 <= N <= 1998:
    print('ABD')
else:
    print('IDK')
