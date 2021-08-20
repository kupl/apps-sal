s = input()
k = int(input())
min_l = max_l = 0
for c in s:
    if c == '?' or c == '*':
        min_l -= 1
    else:
        min_l += 1
        max_l += 1
if k < min_l or (k > max_l and '*' not in s):
    print('Impossible')
else:
    r = ''
    d = k - min_l
    l = len(s)
    for i in range(l):
        if i + 1 < l and s[i + 1] == '?':
            if d > 0:
                r += s[i]
                d -= 1
        elif i + 1 < l and s[i + 1] == '*':
            while d > 0:
                r += s[i]
                d -= 1
        elif s[i] != '?' and s[i] != '*':
            r += s[i]
    print(r)
