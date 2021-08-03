# A - One Card Poker

# 一枚ポーカーの勝敗を判定し出力する


card_A, card_B = list(map(int, input().split()))

if card_A == 1:
    card_A = 14

if card_B == 1:
    card_B = 14

if card_A > card_B:
    print('Alice')
elif card_A < card_B:
    print('Bob')
elif card_A == card_B:
    print('Draw')
