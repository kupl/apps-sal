n = int(input())
d = {}
l = 0
r = 0
for i in range(n):
    s = input().split()
    if s[0] == 'R':
        d[s[1]] = [1, r]
        r += 1
    if s[0] == 'L':
        d[s[1]] = [0, l]
        l += 1
    if s[0] == '?':
        if d[s[1]][0] == 0:
            print(min(l - d[s[1]][1] - 1, d[s[1]][1] + r))
        else:
            print(min(r - d[s[1]][1] - 1, l + d[s[1]][1]))
