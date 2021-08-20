s = input()
x = 1
if len(s) % 2 == 1:
    print('No')
else:
    x = len(s) - 1
    start = 1
    while len(s) != x:
        x = len(s)
        n = x
        for i in range(max(start, 1), x):
            l = i - 1
            r = i
            if s[l] == s[r]:
                while l >= 0 and r < n and (s[l] == s[r]):
                    r += 1
                    l -= 1
                l += 1
                r -= 1
                s = s[:l] + s[r + 1:]
                start = l
                break
    if len(s) == 0:
        print('Yes')
    else:
        print('No')
