import sys
import io
fin = io.StringIO(sys.stdin.read())
s = fin.readline().strip()
n = len(s)
table = [0] * n
for i in range(n - 1):
    table[i] = int(s[i] == s[i + 1]) + (table[i - 1] if i > 0 else 0)
m = int(fin.readline())
for _ in range(m):
    (l, r) = list(map(int, fin.readline().split()))
    print(table[r - 2] - (table[l - 2] if l > 1 else 0))
