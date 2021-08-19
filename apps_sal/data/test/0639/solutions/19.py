from sys import stdin, stdout


def rint():
    return list(map(int, stdin.readline().split()))


(n, x) = rint()
a = list(rint())
a.sort()
b = [0 for i in range(101)]
for aa in a:
    b[aa] = 1
cnt = 0
for i in range(x):
    if b[i] == 0:
        cnt += 1
if b[x] == 1:
    cnt += 1
print(cnt)
