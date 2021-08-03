import sys
def LS(): return list(sys.stdin.readline().rstrip().split())


N, S = LS()
ans = 0
for i in range(int(N)):
    S1 = S[i:]
    a, g = 0, 0
    for s in S1:
        if s == 'A':
            a += 1
        elif s == 'G':
            g += 1
        elif s == 'C':
            g -= 1
        elif s == 'T':
            a -= 1
        if a == g == 0:
            ans += 1
print(ans)
