from sys import stdin, stdout, exit


def sin():
    return stdin.readline().rstrip()


def listInput():
    return list(map(int, sin().split()))


def printBS(li):
    if not li:
        return
    for i in range(len(li) - 1):
        stdout.write('%d ' % li[i])
    stdout.write('%d\n' % li[-1])


n = int(sin())
ans = 0
for _ in range(n):
    (a, b) = listInput()
    ans = max(ans, a + b)
print(ans)
