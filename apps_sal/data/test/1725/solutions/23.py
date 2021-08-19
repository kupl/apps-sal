(n, m, d) = list(map(int, input().split()))
ll = []
for i in range(n):
    temp = [int(x) for x in input().split()]
    ll.append(temp)
l = []
for i in range(n):
    for j in range(len(ll[i])):
        l.append(ll[i][j])
flag = 0
l = sorted(l)
for i in range(len(l) - 1):
    if abs(l[i] - l[i + 1]) % d != 0:
        flag = 1
        break
median = l[len(l) // 2]
moves = 0
for i in range(len(l)):
    moves += abs(l[i] - median) // d
if flag == 1:
    print(-1)
else:
    print(moves)
