s = input().rstrip()
s += "T"
x, y = list(map(int, input().split()))
cnt = 0
dir = 0
P = [{0}, {0}]
first = True
for i in range(len(s)):
    if s[i] == "F":
        cnt += 1
    else:
        tmp = set()
        if first:
            for p in P[dir % 2]:
                tmp |= {p + cnt}
            first = False
        else:
            for p in P[dir % 2]:
                tmp |= {p + cnt, p - cnt}
        P[dir % 2] = tmp
        dir += 1
        cnt = 0
if x in P[0] and y in P[1]:
    print("Yes")
else:
    print("No")
