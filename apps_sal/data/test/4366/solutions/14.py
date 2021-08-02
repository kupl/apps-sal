# A - Remaining Time

# 現在時刻はA時で、コンテストはB時間後に始まる
# コンテストの開始時刻は、24時間表記で何時か？


A, B = list(map(int, input().split()))

answer = A + B

if answer < 24:
    print(answer)
else:
    print((answer - 24))
