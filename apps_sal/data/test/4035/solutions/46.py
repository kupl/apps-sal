import math
(a, b) = map(int, input().split())
ast = math.ceil(a * 12.5)
aend = math.ceil((a + 1) * 12.5) - 1
bst = b * 10
bend = (b + 1) * 10 - 1
flag = 0
for i in range(bst, bend + 1):
    if ast <= i <= aend:
        print(i)
        flag = 1
        break
if flag == 0:
    print(-1)
