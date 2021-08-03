import re


def getAnswer(x):
    if len(x) < 5:
        return "Too weak"
    if (re.search('[A-Z]', x)) == None:
        return "Too weak"
    if (re.search('[a-z]', x)) == None:
        return "Too weak"
    if (re.search('[0-9]', x)) == None:
        return "Too weak"
    return "Correct"


def main():
    x = input()
    print(getAnswer(x))


main()
