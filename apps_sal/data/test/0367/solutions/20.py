import string


def main():
    s = input()
    print(makePalindrome(s))


def makePalindrome(s):
    letters = 26
    lCounts = [0] * letters
    for c in s:
        lCounts[ord(c) - ord('a')] += 1
    odds = [i for i in range(letters) if lCounts[i] % 2 != 0]
    if len(s) % 2 == 0:
        for i in range(len(odds) // 2):
            lCounts[odds[i]] += 1
        for i in range(len(odds) // 2, len(odds)):
            lCounts[odds[i]] -= 1
        return countsToPalindrome(lCounts, 0)
    else:
        for i in range(len(odds) // 2):
            lCounts[odds[i]] += 1
        for i in range(len(odds) // 2 + 1, len(odds)):
            lCounts[odds[i]] -= 1
        return countsToPalindrome(lCounts, 0)


def countsToPalindrome(L, i, middle=""):
    if i == len(L):
        return middle
    elif L[i] % 2 == 0:
        letter = string.ascii_lowercase[i]
        return (letter * (L[i] // 2)) + \
            countsToPalindrome(L, i + 1, middle) + \
            (letter * (L[i] // 2))
    else:
        letter = string.ascii_lowercase[i]
        return (letter * ((L[i] - 1) // 2)) + \
            countsToPalindrome(L, i + 1, letter) + \
            (letter * ((L[i] - 1) // 2))


main()
