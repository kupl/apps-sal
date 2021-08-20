s = input()
x = 0
for i in s:
    c = 0
    for j in s:
        if i == j:
            c += 1
    if c != 1:
        print('no')
        break
    else:
        x += 1
        if x == len(s):
            print('yes')
            break
