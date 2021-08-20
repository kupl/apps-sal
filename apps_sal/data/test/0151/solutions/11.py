vowel = ['a', 'e', 'i', 'o', 'u']
st = input()
num = 0
same_let = 0
last_let = ''
for ch in st:
    if ch in vowel:
        num = 0
        same_let = 0
        let = ''
        print(ch, end='')
    else:
        num += 1
        if ch == last_let or last_let == '':
            last_let = ch
            same_let += 1
        else:
            last_let = ch
            same_let = 1
        if num >= 3 and same_let < 3:
            print(' ', end='')
            num = 1
            same_let = 1
            last_let = ch
        print(ch, end='')
