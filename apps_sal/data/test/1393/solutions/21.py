def tanya_and_postcard(tanya_message, newspaper_letters):
    difference = ord('a') - ord('A')
    yays_count = 0
    whoopses_count = 0
    letters_counts = get_letters_counts(newspaper_letters)

    tanya_message = list(tanya_message)

    for index in range(0, len(tanya_message)):
        letter = tanya_message[index]

        if (letter in letters_counts) and (letters_counts[letter] > 0):
            letters_counts[letter] -= 1
            yays_count += 1
            tanya_message[index] = chr(0)

    for letter in tanya_message:
        letter = get_letter_in_opposite_casing(letter)

        if (letter in letters_counts) and (letters_counts[letter] > 0):
            letters_counts[letter] -= 1
            whoopses_count += 1

    return {'yays_count': yays_count, 'whoopses_count': whoopses_count}


def get_letters_counts(letters):
    letters_counts = {}

    for letter in letters:
        if letter in letters_counts:
            letters_counts[letter] += 1
        else:
            letters_counts[letter] = 1

    return letters_counts


def get_letter_in_opposite_casing(letter):
    if letter.islower():
        return letter.upper()
    else:
        return letter.lower()


def main():
    tanya_message = input()
    newspaper_letters = input()

    result = tanya_and_postcard(tanya_message, newspaper_letters)
    print('{0} {1}'.format(result['yays_count'], result['whoopses_count']))


def __starting_point():
    main()


__starting_point()
