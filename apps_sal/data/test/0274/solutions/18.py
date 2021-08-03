n = input()
s = input()

b = 0
maxb = 0
for c in s:
    if c == '[':
        b += 1
    else:
        b -= 1
    if b > maxb:
        maxb = b

res = [""] * (maxb * 2 + 1)
b = maxb
pred = ""

for k in range(len(s)):
    c = s[k]

    if c == '[':
        if k != len(s) - 1:
            if s[k + 1] == ']':
                sep = '| '
            else:
                sep = '|'
        else:
            sep = '|'

        i = maxb - b
        for j in range(i):
            res[j] += ' '

        res[i] += '+-'
        for j in range(i + 1, len(res) - i - 1):
            res[j] += sep
        res[len(res) - i - 1] += '+-'

        for j in range(len(res) - i, len(res)):
            res[j] += ' '

        pred = '['
        b -= 1

    elif c == ']':
        if k != len(s) - 1:
            if s[k + 1] == '[':
                space = '   '
            else:
                space = ' '
        else:
            space = ' '

        b += 1
        if pred == '[':
            sep = ' |'
            for j in range(len(res)):
                res[j] += ' '
        else:
            sep = '|'

        i = maxb - b
        for j in range(i):
            res[j] += space

        res[i] += '-+'
        for j in range(i + 1, len(res) - i - 1):
            res[j] += sep
        res[len(res) - i - 1] += '-+'

        for j in range(len(res) - i, len(res)):
            res[j] += space

        pred = ']'

for i in res:
    print(i)
