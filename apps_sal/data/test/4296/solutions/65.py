cards = list(map(int, input().split()))
print('win' if sum(cards) <= 21 else 'bust')
