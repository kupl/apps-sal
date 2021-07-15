a = [i for i in input()]
for i in range(26):
    a += [chr(ord(a[i]) + ord('A') - ord('a'))]
b = [i for i in input()]
for i in range(26):
    b += [chr(ord(b[i]) + ord('A') - ord('a'))]
d = {a[i]: b[i] for i in range(52)}
s = input()
for i in s:
    if i in d:
        print(d[i], end='')
    else:
        print(i, end='')
