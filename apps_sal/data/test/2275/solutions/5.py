def solve(s):
    last = -1
    c = 0
    m = 0
    for x in range(len(s)):
        if s[x] == 'A':
            last = x
            c = 0
        elif last != -1:
            c += 1
            m = max(c, m)
    return m


n = int(input())
for x in range(n):
    k = int(input())
    s = input()
    print(solve(s))
