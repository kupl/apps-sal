def getLetterNumber(letter):
    if '0' <= letter <= '9':
        return ord(letter) - ord('0')
    if 'A' <= letter <= 'Z':
        return ord(letter) - ord('A') + 10
    if 'a' <= letter <= 'z':
        return ord(letter) - ord('a') + 36
    if letter == '-':
        return 62
    if letter == '_':
        return 63

def getNumberOfVairants(number):
    return 3**"{0:b}".format(number).zfill(6).count('0')

def getNumber(str):
    result = 1;
    for c in str:
        num = getLetterNumber(c)
        result = result * getNumberOfVairants(num)
        result %= (int(1e9) + 7)
    return result

s = input()
print(getNumber(s))
