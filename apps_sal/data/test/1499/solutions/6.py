(n, m) = [int(i) for i in input().split()]
Seats = [[0, 0, 0, 0] for i in range(n)]
Ans = []
for i in range(m):
    if i + 1 <= 2 * n:
        Seats[i // 2][i % 2] = i + 1
    else:
        j = i - 2 * n
        Seats[j // 2][j % 2 + 2] = i + 1
for i in range(n):
    if Seats[i][2]:
        Ans.append(Seats[i][2])
    if Seats[i][0]:
        Ans.append(Seats[i][0])
    if Seats[i][3]:
        Ans.append(Seats[i][3])
    if Seats[i][1]:
        Ans.append(Seats[i][1])
print(' '.join(map(str, Ans)))
