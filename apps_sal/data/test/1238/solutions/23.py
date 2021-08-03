from sys import stdin, stdout, exit


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


n = int(sin())
li = listInput()

print(max(li) - min(li) + 1 - n)
