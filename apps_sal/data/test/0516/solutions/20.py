import sys
def read(): return sys.stdin.readline().rstrip()
def readi(): return int(sys.stdin.readline())
def writeln(x): return sys.stdout.write(str(x) + "\n")
def write(x): return sys.stdout.write(x)


n, m = list(map(int, read().split()))
s, t = read(), read()

mcnt, midx = -1, -1
for i in range(m - n + 1):
    cnt = 0
    for j in range(n):
        if s[j] == t[j + i]:
            cnt += 1
    if cnt > mcnt:
        mcnt = cnt
        midx = i


k = 0
pos = []
for i in range(n):
    if s[i] != t[midx + i]:
        k += 1
        pos.append(str(i + 1))

writeln(k)
if k:
    writeln(' '.join(pos))
