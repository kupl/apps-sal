# 099A

# N回目(数値）：標準入力
N = int(input())

# 1~999回目：ABC001~ABC999
# 1000~1998回目：ABD001~ABD999
# N回目のコンテストの名前の最初の3文字を出力

if N < 1000:
    print('ABC')
elif 1000 <= N <= 1998:
    print('ABD')
