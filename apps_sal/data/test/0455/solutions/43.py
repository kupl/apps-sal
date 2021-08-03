n = int(input())

P = []
M = []
for _ in range(n):
    x, y = map(int, input().split())
    P.append((x, y))
    M.append((x + y) % 2)

if len(set(M)) == 2:
    print(-1)
    return

D = [1 << i for i in range(31, -1, -1)]
if M[0] == 0:
    D.append(1)

print(len(D))
print(*D, sep=' ')

for x, y in P:
    a = []
    for d in D:
        if abs(x) > abs(y):
            if x < 0:
                a.append('L')
                x += d
            else:
                a.append('R')
                x -= d
        else:
            if y < 0:
                a.append('D')
                y += d
            else:
                a.append('U')
                y -= d
    print(*a, sep='')
