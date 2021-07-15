c = str.lower(input())

def answer(c: str) -> str:
    n = ('a', 'e', 'i', 'o', 'u')

    if c in n:
        return 'vowel'
    else:
        return 'consonant'

print((answer(c)))

