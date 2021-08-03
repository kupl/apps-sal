from sys import stdin, stdout, exit, setrecursionlimit


def sin():
    return stdin.readline().rstrip()


def listInput():
    return list(map(int, sin().split()))


def printBS(li):
    if not li:
        return
    for i in range(len(li) - 1):
        stdout.write("%d " % (li[i]))
    stdout.write("%d\n" % (li[-1]))


t = int(sin())
for _ in range(t):
    a = int(sin())
    s = str(bin(a))[2:]
    print(2**(s.count('1')))
