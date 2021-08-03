k = int(input())
for i in range(k):
    l = int(input())
    s = input()
    t = input()
    d = 0
    sl = []
    tl = []
    for j in range(l):
        if s[j] != t[j]:
            d += 1
            sl.append(s[j])
            tl.append(t[j])
    if d == 0 or (d == 2 and sl[0] == sl[1] and tl[0] == tl[1]):
        print("Yes")
    else:
        print("No")
