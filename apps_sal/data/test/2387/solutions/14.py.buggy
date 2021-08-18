N, *S = open(0)

L = [s.count("(") for s in S]
R = [s.count(")") for s in S]

X = sorted(((s[:-1], r) for s, l, r in zip(S, L, R) if l - r >= 0), key=lambda x: x[1])
Y = sorted(((s[:-1], l) for s, l, r in zip(S, L, R) if l - r < 0), key=lambda x: -x[1])

cnt = 0
for s, _ in X + Y:
    for si in s:
        cnt += 1 if si == "(" else -1
        if cnt < 0:
            print("No")
            return

if cnt == 0:
    print("Yes")
else:
    print("No")
