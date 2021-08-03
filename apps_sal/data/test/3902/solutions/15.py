
def __starting_point():

    word = input()

    suffixes = set()
    possible = set()
    my_set = set()
    not_poss = set()

    possible.add((len(word), 2))

    while possible:
        tam, x = possible.pop()
        a = tam + x
        for i in [x, 5 - x]:
            root = tam - i
            new_pos = (root, i)

            if root < 5 or new_pos in my_set or (word[root:tam] == word[tam:a]):
                not_poss.add(word[root:tam])
            else:
                suffixes.add(word[root:tam])
                possible.add(new_pos)
                my_set.add(new_pos)

    suffixes_alph = sorted(suffixes)

    print(len(suffixes))
    for i in suffixes_alph:
        print(i)


__starting_point()
