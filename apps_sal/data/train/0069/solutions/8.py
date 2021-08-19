import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    (x, y) = list(map(int, input().split()))
    s = list(input())
    if '1' not in s:
        print(0)
    else:
        c = s.index('1')
        d = len(s) - s[::-1].index('1')
        s = s[c:d]
        b = []
        c = 0
        for i in range(len(s)):
            if s[i] == '0':
                c += 1
            else:
                if c != 0:
                    b.append(c)
                c = 0
        s = x
        for i in range(len(b)):
            if b[i] * y > x:
                s += x
            else:
                s += b[i] * y
        print(s)
