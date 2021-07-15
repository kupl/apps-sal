# 入力を受ける
N = int(input())
S = input()

# Nが偶数であるか、奇数であるかみる
# 偶数ならば、半分の位置で区切って、一致するかみて、出力する
print('Yes' if N%2 == 0 and S[0:(N//2)] == S[N//2:N] else 'No')
