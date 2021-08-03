S = input()
K = int(input())

ones = 0
inf = None
for c in S:
    if c == '1':
        ones += 1
    else:
        inf = c
        break

if K <= ones:
    print('1')
else:
    print(inf)
