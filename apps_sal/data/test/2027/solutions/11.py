import sys

fin = sys.stdin
fout = sys.stdout
n = int(fin.readline())
a = list(map(int, fin.readline().split()))
res = [a[-1]]
for i in range(n - 2, -1, -1):
    res.append(a[i + 1] + a[i])
res.reverse()
fout.write(' '.join(map(str, res)))

