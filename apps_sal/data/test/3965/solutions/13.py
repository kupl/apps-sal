from collections import Counter
letters = 'aeiouy'


def getNum(s):
    result = 0
    cc = Counter(s)
    for letter in letters:
        result += cc[letter]
    return result


n = int(input())
p = list(map(int, input().split()))
result = True
for i in range(n):
    line = input()
    result = result and getNum(line.lower()) == p[i]
print({True: 'YES', False: 'NO'}[result])
