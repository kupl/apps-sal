n, cards = int(input()), sorted(input().split())
print(int(max(('555555555' * (cards.count('5') // 9) + '0' * cards.count('0')) * (cards.count('0') != 0), '-1')))

