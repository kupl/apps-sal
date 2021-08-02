# A - HonestOrDishonest

# a, bにそれぞれ文字'H','D'が入力されるので、'H'か'D'を判定し出力する


a, b = input().split()

if a == 'H':
    if b == 'H':
        print('H')
    elif b == 'D':
        print('D')
elif a == 'D':
    if b == 'H':
        print('D')
    elif b == 'D':
        print('H')
