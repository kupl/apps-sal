n = input()
word = input().strip()


def is_vowel(ch):
    return ch in ['a', 'e', 'i', 'o', 'u', 'y']


res = [word[0]]
for i in range(1, len(word)):
    if is_vowel(word[i]):
        if not is_vowel(word[i - 1]):
            res.append(word[i])
    else:
        res.append(word[i])
print(''.join(res))
