table = [[0] * 3 for _ in range(3)]
A = [list(map(int, input().split())) for _ in range(3)]
A = sum(A, [])
N = int(input())
B = [int(input()) for _ in range(N)]
for b in B:
    tmp = [i for (i, x) in enumerate(A) if x == b]
    for t in tmp:
        table[t // 3][t % 3] = 1
flag = False
(n1, n2) = (0, 0)
for i in range(3):
    if sum(table[i]) == 3:
        flag = True
    if sum([table[j][i] for j in range(3)]) == 3:
        flag = True
    n1 += table[i][i]
    n2 += table[i][2 - i]
if n1 == 3 or n2 == 3:
    flag = True
if flag:
    print('Yes')
else:
    print('No')
