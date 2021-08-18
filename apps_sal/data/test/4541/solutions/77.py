
def atc_049a(c: str) -> str:
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        return "vowel"
    else:
        return "consonant"


c = input()
print((atc_049a(c)))
