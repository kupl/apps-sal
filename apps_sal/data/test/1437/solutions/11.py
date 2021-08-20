cyph = [str(x) for x in range(10)] + [chr(65 + i) for i in range(26)] + [chr(97 + i) for i in range(26)] + ['-'] + ['_']
dct = {}


def decod(char):
    i = 0
    if char in dct:
        return dct[char]
    else:
        while cyph[i] != char:
            i += 1
        dct[char] = i
        return i


dct2 = {}


def zeros(i):
    if i in dct2:
        return dct2[i]
    else:
        cct = 0
        for j in range(6):
            cct += (i >> j) % 2
        dct2[i] = 6 - cct
        return dct2[i]


s = input()
cnt = 1
for char in s:
    tmp = decod(char)
    cnt *= 3 ** zeros(tmp)
    cnt %= 1000000007
print(cnt)
