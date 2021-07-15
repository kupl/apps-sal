import itertools


input()
cards = tuple(set(str.split(input())))
n = len(cards)

if n == 1:

    print(0)
    return

symbols = "RGBYW12345"
for l in range(1, 10):

    for comb in itertools.combinations(symbols, l):

        positions = [cards] * n
        for symbol in comb:

            for i in range(n):

                if symbol in cards[i]:

                    positions[i] = tuple([c for c in positions[i] if symbol in c])

                else:

                    positions[i] = tuple([c for c in positions[i] if symbol not in c])

        if sum(map(len, positions)) == n:

            print(l)
            return

