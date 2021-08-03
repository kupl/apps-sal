x = input()
ch = nch = 0
for i in 'abcdefghijklmnopqrstuvwxyz':
    if x.count(i) > 0:
        if x.count(i) % 2 == 0:
            ch += 1
        else:
            nch += 1

t = 0
while nch > 1:
    if ch > 0:
        ch -= 1
        nch += 1
    else:
        nch -= 1
    t = (t + 1) % 2
print('First' if t == 0 else 'Second')
