cards_map = {}
cards_map['A'] = list(input().upper())
cards_map['B'] = list(input().upper())
cards_map['C'] = list(input().upper())
current = 'A'
while True:
    if len(cards_map[current]) == 0:
        break
    else:
        current = cards_map[current].pop(0)
print(current)
