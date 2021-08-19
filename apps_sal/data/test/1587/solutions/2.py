input()
problem = input()
stones = []
rs = []
W = 0
R = 0
for s in problem:
    if s == 'R':
        stones.append(1)
        R += 1
    else:
        stones.append(0)
rs.append(max(W, R))
for i in range(len(stones)):
    if stones[i] == 0:
        W += 1
    else:
        R -= 1
    rs.append(max(W, R))
print(min(rs))
