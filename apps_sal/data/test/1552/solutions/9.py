n = int(input())
t = [int(s) for s in input().split()]

teams = [[0, 0, 0] for i in range(n)]
n1, n2, n3 = 0, 0, 0
for i in range(n):
    if t[i] == 1:
        teams[n1][0] = i + 1
        n1 += 1
    elif t[i] == 2:
        teams[n2][1] = i + 1
        n2 += 1
    else:
        teams[n3][2] = i + 1
        n3 += 1
w = min(n1, n2, n3)
print(w)
if w > 0:
    for k in range(w):
        print(' '.join(map(str, teams[k])))
