from sys import stdin, stdout


def main():
    h, w = map(int, stdin.readline().split())
    ver = set()
    hor = set()
    for i in range(h):
        s = stdin.readline().rstrip()
        for j in range(w):
            if s[j] == '*':
                hor.add(j)
                ver.add(i)
    stdout.write(str(max(max(hor) - min(hor), max(ver) - min(ver)) + 1))


main()
