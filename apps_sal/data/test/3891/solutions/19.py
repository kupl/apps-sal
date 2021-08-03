n, M = [int(x) for x in input().split()]
m = []
for i in range(n):
    m.append(input())
c = 0
idx = []
idx2 = []
for i in range(n):
    for j in range(M):
        if m[i][j] == 'B':
            idx.append(i)
            idx2.append(j)
            c += 1
ans1 = sum(idx) // c + 1
ans2 = sum(idx2) // c + 1
print(ans1, ans2)
