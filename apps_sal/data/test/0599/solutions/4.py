palindrom = lambda s: s == s[::-1]
printans = lambda l: print(''.join(l))
s = list(input())

for i in range(len(s) + 1):
    for letter in 'abcdefghijklmnopqrstvwuxyz':
        tmp = s[:]
        tmp.insert(i, letter)
        if palindrom(tmp):
            printans(tmp)
            return

print('NA')
