R = 'R'
S = 'S'
P = 'P'


def winner(a, b):
    if a == b:
        return a
    if a != R and b != R:
        return S
    if a != S and b != S:
        return P
    if a != P and b != P:
        return R


(n, k) = map(int, input().split())
s = input()
s = s + s
for _ in range(k):
    ns = ''
    for i in range(n):
        ns += winner(s[2 * i], s[2 * i + 1])
    s = ns + ns
print(s[0])
