import sys
T = int(input())
for i in range(T):
    n = int(input())
    s = input()
    (l, r) = (0, n - 1)
    out = False
    while r > l:
        t = abs(ord(s[r]) - ord(s[l]))
        if t != 0 and t != 2:
            print('NO')
            out = True
            break
        l += 1
        r -= 1
    if not out:
        print('YES')
