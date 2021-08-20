from sys import stdin, exit


def listInput():
    return list(map(int, stdin.readline().rstrip().split()))


(n, m) = listInput()
li = listInput()
rem = 0
ans = []
for i in li:
    ans.append((i + rem) // m)
    rem = (i + rem) % m
print(' '.join([str(i) for i in ans]))
