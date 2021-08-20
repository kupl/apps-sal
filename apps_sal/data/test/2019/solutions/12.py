from sys import exit, stdin, stderr


def rl():
    return [int(w) for w in stdin.readline().split()]


(T,) = rl()
for _ in range(T):
    s = input().rstrip()
    c0 = len([c for c in s if c == '0'])
    c1 = len([c for c in s if c == '1'])
    print(['NET', 'DA'][min(c0, c1) & 1])
