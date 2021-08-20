s = input()
(x, y) = map(int, input().split())
FT_1 = [0]
FT_2 = [0]
state = 1
for a in s:
    if a == 'T':
        if state == 1:
            state = 2
            FT_2.append(0)
        else:
            state = 1
            FT_1.append(0)
    elif state == 1:
        FT_1[-1] += 1
    else:
        FT_2[-1] += 1
DP_1 = 1
x -= FT_1[0]
x -= -sum(FT_1[1:])
DP_2 = 1
y -= FT_2[0]
y -= -sum(FT_2[1:])
for v in FT_1[1:]:
    DP_1 |= DP_1 << 2 * v
for v in FT_2[1:]:
    DP_2 |= DP_2 << 2 * v
if x >= 0 and y >= 0 and DP_1 >> x & 1 and DP_2 >> y & 1:
    print('Yes')
else:
    print('No')
'\nprint(x,y)\nprint(FT_1)\nprint(FT_2)\nprint(DP_1)\nprint(DP_2)\n'
