def palindrome(s):
    chars = [0] * 26
    L = len(s)
    isOdd = (L % 2 != 0)
    for c in s:
        n = ord(c) - 97
        chars[n] += 1

    left = 0
    right = 25
    while left < right:
        while left < 25 and chars[left] % 2 == 0:
            left += 1
        while right > 0 and chars[right] % 2 == 0:
            right -= 1
        if left < 25 and right > 0:
            if left == right and isOdd:
                break
            else:
                chars[left] += 1
                chars[right] -= 1

    result = [' '] * L
    index = 0
    oddC = ""
    for j in range(26):
        n = chars[j]
        if n > 0:
            if n % 2 != 0:
                oddC = chr(j + 97)
            for k in range(n // 2):
                result[index] = chr(j + 97)
                result[L - 1 - index] = chr(j + 97)
                index += 1

    if isOdd:
        result[L // 2] = oddC

    return ''.join(result)


def __starting_point():
    s = input()
    result = palindrome(s)
    print(result)


__starting_point()
