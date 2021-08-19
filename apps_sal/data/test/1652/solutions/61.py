s = list(input())
s.reverse()
s = ''.join(map(str, s))
count = 0
word = ['maerd', 'remaerd', 'resare', 'esare']
while count <= len(s) - 8:
    counttemp = count
    for i in range(4):
        w = word[i]
        if s[count:count + len(w)] == w:
            count += len(w)
    if counttemp == count:
        break
if s[count:] in word or s[count:] == '':
    print('YES')
else:
    print('NO')
