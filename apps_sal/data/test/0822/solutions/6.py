import sys
fin = sys.stdin
fout = sys.stdout
ans = 0
(n, m, z) = list(map(int, fin.readline().split()))
for i in range(1, z + 1):
    if i % n == 0 and i % m == 0:
        ans += 1
fout.write(str(ans))
