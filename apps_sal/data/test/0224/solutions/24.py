import sys
fin = sys.stdin
fout = sys.stdout
m = -1
gl = {'A', 'E', 'I', 'O', 'U', 'Y'}
s = fin.readline().strip()
cur = -1
for i in range(len(s)):
    if s[i] in gl:
        m = max(m, i - cur)
        cur = i
m = max(m, len(s) - cur)
fout.write(str(m))
