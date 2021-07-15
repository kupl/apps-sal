n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

s2 = 2 * n
s4 = n
s1 = 0

tmp = sum([ai // 4 for ai in a])
s4 -= min(tmp, n)
s2 -= 2 * max(tmp - n, 0)

for ai in a:
    if ai % 4 == 2:
        if 0 < s2:
            s2 -= 1
        elif 0 < s4:
            s4 -= 1
            s1 += 1
        else:
            s1 -= 2

for ai in a:
    if ai % 4 == 1:
        if 0 < s1:
            s1 -= 1
        elif 0 < s2:
            s2 -= 1
        else:
            s4 -= 1
            s2 += 1

for ai in a:
    if ai % 4 == 3:
        if 0 < s4:
            s4 -= 1
        elif 1 < s2:
            s2 -= 2
        elif 1 == s2:
            s2 -= 1
            s1 -= 1
        else:
            s1 -= 3

if 0 <= s1 and 0 <= s2 and 0 <= s4:
    print("YES")
else:
    print("NO")

