s = input()
n = len(s)
# l=list(map(int,input().split()))
la = []
lb = []
lc = []
if len(set(s)) == 1:
    print('0')
elif 'a' and 'b' and 'c' in s:
    for i in range(n):
        if s[i] == "a":
            la.append(i)
        elif s[i] == "b":
            lb.append(i)
        elif s[i] == "c":
            lc.append(i)
    # print(la,lb,lc)
    a1, a0 = max(la), min(la)
    b1, b0 = max(lb), min(lb)
    c1, c0 = max(lc), min(lc)
    print(max(abs(a0 - b1), abs(a0 - c1), abs(a1 - b0), abs(a1 - c0), abs(b0 - c1), abs(b1 - c0)))
else:
    r = list(set(s))

    for i in range(n):
        if s[i] == r[0]:
            la.append(i)
        elif s[i] == r[1]:
            lb.append(i)

    # print(la,lb,lc)
    a1, a0 = max(la), min(la)
    b1, b0 = max(lb), min(lb)
    # c1,c0=max(lc),min(lc)
    print(max(abs(a0 - b1), abs(a1 - b0)))
