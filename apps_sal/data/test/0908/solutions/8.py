import sys
line = sys.stdin.readlines()
n = int(line[0])
c = list(map(int, line[1].split()))

INF = 1e16
p, pr = '', ''
c0, cr = 0, 0
for i in range(n):
    s = line[i + 2].rstrip('\r\n')
    sr = s[::-1]
    c00 = c0 if p <= s else INF
    cr0 = cr if pr <= s else INF
    c0r = c0 + c[i] if p <= sr else INF
    crr = cr + c[i] if pr <= sr else INF

    p, pr = s, sr
    c0, cr = min(c00, cr0), min(c0r, crr)

ans = min(c0, cr)
if ans >= INF:
    print(-1)
else:
    print(ans)
