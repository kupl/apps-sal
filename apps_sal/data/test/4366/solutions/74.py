# 現在A時、B時間後に始まるコンテストの開始時刻

A, B = map(int, input().split())
start = A + B

if start >= 24:
    print(start - 24)
else:
    print(start)
