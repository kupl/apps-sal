alpha = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
s = ''
for _ in range(n):
    s += input() + ' '
for x in alpha:
    if x not in s:
        print(x)
        break
else:
    for i in alpha:
        for j in alpha:
            if i + j not in s:
                print(i + j)
                quit()
