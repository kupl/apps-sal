import sys


def main():
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()
    c = sys.stdin.readline().rstrip()
    x = {}
    for i in range(len(a)):
        x[a[i]] = b[i]
        x[a[i].upper()] = b[i].upper()
    s = [0] * len(c)
    for i in range(len(c)):
        if c[i] in x:
            s[i] = x[c[i]]
        else:
            s[i] = c[i]
    print(''.join(s))


main()
