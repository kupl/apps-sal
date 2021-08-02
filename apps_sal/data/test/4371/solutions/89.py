# B - 754

# 1～9からなる文字列Sから連続する3文字を取り出す
# 取り出した文字列と753との差の絶対値は最小でいくつか出力する

S = input()
answer = 999

for i in range(len(S) - 2):
    num = int(S[i] + S[i + 1] + S[i + 2])
    if answer > abs(num - 753):
        answer = abs(num - 753)

print(answer)
