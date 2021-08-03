import sys
line = sys.stdin.readlines()
n = int(line[0])
c = list(map(int, line[1].split()))

no = (0, '')
yes = (0, '')
for i in range(n):
    s = line[i + 2].rstrip('\r\n')
    sr = s[::-1]
    nn, ny, yn, yy = 1e16, 1e16, 1e16, 1e16
    if s >= no[1]:
        nn = no[0]
    if sr >= no[1]:
        ny = no[0] + c[i]
    if s >= yes[1]:
        yn = yes[0]
    if sr >= yes[1]:
        yy = yes[0] + c[i]
    no = (min(nn, yn), s)
    yes = (min(ny, yy), sr)

ans = min(no[0], yes[0])
if ans > 1e15:
    print(-1)
else:
    print(ans)
