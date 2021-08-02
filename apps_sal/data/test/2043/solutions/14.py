s = input()
t = input()
if len(t) <= len(s):
    print(0)
elif len(s) == 1:
    p1 = t.find(s)
    p2 = t.rfind(s)
    if p2 - p1 == 0:
        print(0)
    else:
        print(p2 - p1)
else:
    p1 = 0
    for i in range(len(s)):
        while s[i] != t[p1]:
            p1 += 1
        else:
            p1 += 1
    p1 -= 1
    p2 = len(t) - 1
    for i in range(len(s) - 1, -1, -1):
        while s[i] != t[p2]:
            p2 -= 1
        else:
            p2 -= 1
    p2 += 1
    if p2 - p1 <= 0:
        print(0)
    else:
        print(p2 - p1)
