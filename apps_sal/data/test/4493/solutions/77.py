c = []
for i in range(3):
    c.append([int(i) for i in input().split()])
(a1, a2, a3) = [0, c[1][1] - c[0][1], c[2][1] - c[0][1]]
(b1, b2, b3) = [c[0][0], c[0][1], c[0][2]]
ans = [[a1 + b1, a1 + b2, a1 + b3], [a2 + b1, a2 + b2, a2 + b3], [a3 + b1, a3 + b2, a3 + b3]]
if ans == c:
    print('Yes')
else:
    print('No')
