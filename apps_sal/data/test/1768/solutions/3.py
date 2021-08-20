import sys
n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
ans = [[-1] * (n + 1) for x in range(26)]
for c in range(26):
    for l in range(n):
        nrOfC = 0
        for r in range(l, n):
            if s[r] == chr(97 + c):
                nrOfC += 1
            ans[c][r - l + 1 - nrOfC] = max(ans[c][r - l + 1 - nrOfC], r - l + 1)
for i in range(int(sys.stdin.readline().strip())):
    (m, c) = sys.stdin.readline().strip().split()
    m = int(m)
    print(ans[ord(c) - 97][m] if ans[ord(c) - 97][m] != -1 else n)
