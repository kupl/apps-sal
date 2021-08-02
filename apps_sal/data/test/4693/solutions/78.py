# A - Restricted

# A+Bの値を出力する
# A+Bが10以上の場合はerrorと出力する


A, B = list(map(int, input().split()))

answer = A + B

if answer < 10:
    print(answer)
else:
    print('error')
