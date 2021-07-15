from sys import stdin

t  = int(stdin.readline())
for q in range(t):
    n = int(stdin.readline())
    m1, m2 = 10**9+1, 0
    for i in range(n):
        l, r = list(map(int, stdin.readline().split()))
        m1 = min(m1, r)
        m2 = max(m2, l)
    print(max(0, m2 - m1))

