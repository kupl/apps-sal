import sys
3


slika = """+------------------------+
|
|
|
|
+------------------------+"""


def __starting_point():
    st = int(sys.stdin.readline())
    lines = [list(line) for line in slika.split('\n')]
    w = min(len(line) for line in lines)
    for k in range(w):
        if st == 0:
            break
        for l in range(len(lines)):
            if st == 0:
                break
            if lines[l][k] == '
            lines[l][k] = 'O'
            st -= 1

    for line in lines:
        print(''.join(line))


__starting_point()
