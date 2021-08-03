def out(M, p):
    if p == 0:
        return M
    else:
        out = '{0}E{1}'.format(M, p)
        return out


res = 0
a = 0
inp = list(str(input()))
for it in '123456789':
    if (it in inp) == True:
        res += 1
if res == 0:
    res = -1
    print('0')
else:
    res = 0
while res == 0:
    res -= 1
    i = 0
    k = 0
    while inp[k] == '0':
        k += 1
    inp = inp[k:]

    if inp[0] == '.':
        inp.insert(0, '0')
    if inp[len(inp) - 1] == '.':
        inp.remove(inp[len(inp) - 1])

    if ('.' in inp) == True:
        while True:
            if inp[i] != '.':
                i += 1
            else:
                break

        inp.reverse()
        k = 0
        while inp[k] == '0':
            k += 1
        inp = inp[k:]
        if inp[0] == '.':
            inp.remove('.')
        inp.reverse()
        res -= 1

        if ('.' in inp) == False:
            i = len(inp)
            inp.insert(1, '.')
            inp.reverse()
            k = 0
            while inp[k] == '0':
                k += 1
            inp = inp[k:]
            while inp[0] == '.':
                inp.remove('.')
            inp.reverse()
            inp = ''.join(inp)
            a -= 1
            print(out(inp, i - 1))
        if ('.' in inp) == True and len(inp[:i]) == 1:
            i = 0
            if inp[0] == '0':
                inp.remove('.')
                k = 0
                while inp[i] == '0':
                    i += 1
                inp = inp[i:]
                inp.insert(1, '.')
            if inp[len(inp) - 1] == '.':
                inp.remove('.')
            a = -1
            print(out(''.join(inp), -i))
        if ('.' in inp) == True and len(inp[:i]) > 1 and a == 0:
            inp.remove('.')
            inp.insert(1, '.')
            inp = ''.join(inp)
            print(out(inp, i - 1))

    else:
        i = len(inp)
        inp.insert(1, '.')
        inp.reverse()
        k = 0
        while inp[k] == '0':
            k += 1
        inp = inp[k:]
        while inp[0] == '.':
            inp.remove('.')
        inp.reverse()
        inp = ''.join(inp)
        print(out(inp, i - 1))
