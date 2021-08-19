s = input()
(nb, ns, nc) = map(int, input().split())
(pb, ps, pc) = map(int, input().split())
n = int(input())
b = 0
ss = 0
c = 0
for i in range(len(s)):
    if s[i] == 'B':
        b += 1
    if s[i] == 'C':
        c += 1
    if s[i] == 'S':
        ss += 1


def check(m):
    B = m * b
    S = m * ss
    C = m * c
    nn = n
    if B > nb:
        nn -= (B - nb) * pb
    if S > ns:
        nn -= (S - ns) * ps
    if C > nc:
        nn -= (C - nc) * pc
    return nn >= 0


l = 0
r = 10 ** 12 + 1000
while r - l > 1:
    m = l + (r - l) // 2
    if check(m):
        l = m
    else:
        r = m
print(l)
