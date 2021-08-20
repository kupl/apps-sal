n = int(input())
a = []
for i in range(n):
    a.append(input())
if 'E' * n in a and ('E',) * n in list(zip(*a)):
    print(-1)
elif 'E' * n in a:
    for (j, s) in enumerate([''.join(x) for x in zip(*a)]):
        for (i, c) in enumerate(s):
            if c == '.':
                print(i + 1, j + 1)
                break
else:
    for (i, s) in enumerate(a):
        for (j, c) in enumerate(s):
            if c == '.':
                print(i + 1, j + 1)
                break
