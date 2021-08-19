msg = input()
l = input()
msg = list(msg)
d = {}
y = 0
w = 0
for i in l:
    if i not in d:
        d[i] = 0
    d[i] += 1
for j in range(len(msg)):
    i = msg[j]
    if i in d and d[i] > 0:
        d[i] -= 1
        y += 1
        msg[j] = chr(30)
for i in msg:
    if ord(i) >= 97:
        if chr(ord(i) - 32) in d and d[chr(ord(i) - 32)] > 0:
            w += 1
            d[chr(ord(i) - 32)] -= 1
    elif chr(ord(i) + 32) in d and d[chr(ord(i) + 32)] > 0:
        d[chr(ord(i) + 32)] -= 1
        w += 1
print(y, w)
