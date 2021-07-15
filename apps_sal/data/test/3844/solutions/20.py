n = int(input().strip())
ns = list(map(int, input().strip().split()))

from collections import Counter

cards = Counter(ns)
#print(cards)

# given largest cards, invariant is parity of copies
parities = sorted([item for item in cards.items()], reverse=True)
for val, copies in parities:
    if copies % 2:  # odd copies off largest card
        print('Conan')
        break
else:
    print('Agasa')
