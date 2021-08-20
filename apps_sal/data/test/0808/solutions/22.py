def main():
    s = input()
    print(solver(s))


def solver(s):
    s = s[firstNonLeadingZero(s):]
    dotIndex = s.find('.')
    result = None
    if dotIndex == -1:
        s += '.'
        dotIndex = len(s) - 1
    s = s[:firstTrailingZero(s)]
    if dotIndex == 0:
        firstIndex = firstNonZeroDigit(s)
        if firstIndex == -1:
            return '0'
        elif firstIndex == len(s) - 1:
            result = '{}E{}'.format(s[firstIndex], -firstIndex)
        else:
            result = '{}.{}E{}'.format(s[firstIndex], s[firstIndex + 1:], -firstIndex)
    elif dotIndex == 1:
        if len(s) == 2:
            return s[0]
        else:
            return s
    else:
        digits = s[:dotIndex] + s[dotIndex + 1:]
        digits = digits[:firstTrailingZero(digits)]
        if digits[1:] == '0' * (len(digits) - 1):
            result = '{}E{}'.format(digits[0], dotIndex - 1)
        else:
            result = '{}.{}E{}'.format(digits[0], digits[1:], dotIndex - 1)
    return result


def firstNonZeroDigit(s):
    for i in range(len(s)):
        if s[i] not in ['.', '0']:
            return i
    return -1


def firstTrailingZero(s):
    index = len(s) - 1
    while s[index] == '0':
        index -= 1
    return index + 1


def firstNonLeadingZero(s):
    index = 0
    while s[index] == '0':
        index += 1
    return index


main()
