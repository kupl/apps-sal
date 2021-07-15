
VOWELS = ('a', 'e', 'i', 'o', 'u')

def main():
    buf = input()
    n = int(buf)
    s = []
    for i in range(n):
        buf = input()
        s.append(buf)
    word_info = []
    for i, x in enumerate(s):
        vowel_count = 0
        last_vowel = None
        for c in x:
            if c in VOWELS:
                vowel_count += 1
                last_vowel = c
        word_info.append((i, vowel_count, last_vowel))
    word_info.sort(key=lambda x: (x[1], x[2]))
    word_pair = []
    word_pair_first_only = []
    last_vowel_count = 0
    last_last_vowel = None
    last_word = None
    last_word_leftover = None
    for i, x in enumerate(word_info):
        if x[1] > last_vowel_count:
            if last_word and last_word_leftover:
                word_pair_first_only.append((last_word, last_word_leftover))
            last_word_leftover = None
            last_word = None
            last_vowel_count = x[1]
            last_last_vowel = x[2]
        if x[2] != last_last_vowel:
            if last_word:
                if last_word_leftover:
                    word_pair_first_only.append((last_word, last_word_leftover))
                    last_word_leftover = None
                else:
                    last_word_leftover = last_word
                last_word = None
            last_last_vowel = x[2]
        if last_word:
            word_pair.append((last_word, x))
            last_word = None
        else:
            last_word = x
    if last_word and last_word_leftover:
        word_pair_first_only.append((last_word, last_word_leftover))
    lyrics = []
    first_only_pointer = 0
    last_word_pair = None
    for i, x in enumerate(word_pair):
        if first_only_pointer < len(word_pair_first_only):
            last_word_pair = word_pair_first_only[first_only_pointer]
            first_only_pointer += 1
        if last_word_pair:
            lyrics.append((last_word_pair, x))
            last_word_pair = None
        else:
            last_word_pair = x
    print(len(lyrics))
    for x in lyrics:
        print(s[x[0][0][0]], s[x[1][0][0]])
        print(s[x[0][1][0]], s[x[1][1][0]])


def __starting_point():
    main()

__starting_point()
