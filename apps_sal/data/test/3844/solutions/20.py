from collections import Counter
n = int(input().strip())
ns = list(map(int, input().strip().split()))


cards = Counter(ns)

parities = sorted([item for item in cards.items()], reverse=True)
for val, copies in parities:
    if copies % 2:
        print('Conan')
        break
else:
    print('Agasa')
