from sys import stdin
for _ in range(int(stdin.readline())):
    inp = int(stdin.readline())
    if inp < 4:
        print('-1')
    else:
        odd = list(range(5, inp + 1, 2))
        odd.reverse()
        even = list(range(6, inp + 1, 2))
        r = odd + [3, 1, 4, 2] + even
        print(' '.join(map(str, r)))
