import string
input()  # ignore length of word
already_revealed = input()

n = int(input())

indeces = [i for i, x in enumerate(already_revealed) if x == "*"]
revealed_letters = set(already_revealed)

end_set = set(string.ascii_lowercase + "%")
for i in range(n):
    word = input()

    # check word
    word_ok = True
    for i, char in enumerate(word):
        if i not in indeces:
            if already_revealed[i] != char:
                word_ok = False

    if not word_ok:
        continue

    possible_letters = set(word[index] for index in indeces)
    if len(possible_letters.intersection(revealed_letters)) > 0:
        continue

    end_set = possible_letters.intersection(end_set)

if len(end_set) == 27:
    print(0)
else:
    print(len(end_set))
