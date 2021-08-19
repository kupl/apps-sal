import sys
lines = sys.stdin.readlines()
T = int(lines[0].strip())
# (N, K) = map(int, lines[0].strip().split(" "))
for t in range(T):
    (a, b, n, m) = map(int, lines[t + 1].strip().split(" "))
    res = True
    if n + m > a + b:
        res = False
    elif m > min(a, b):
        res = False
    if res:
        print("Yes")
    else:
        print("No")
