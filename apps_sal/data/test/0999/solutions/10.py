n = int(input())
chess = list()
for i in range(n):
    (a, b) = list(map(int, input().split()))
    chess.append([a, b])
m = int(input())
pro = list()
for i in range(m):
    (a, b) = list(map(int, input().split()))
    pro.append([a, b])
(l1, e1, l2, e2) = (0, 1000000000, 0, 1000000000)
for i in range(n):
    l1 = max(chess[i][0], l1)
    e1 = min(chess[i][1], e1)
for i in range(m):
    l2 = max(pro[i][0], l2)
    e2 = min(pro[i][1], e2)
print(max([0, l2 - e1, l1 - e2]))
