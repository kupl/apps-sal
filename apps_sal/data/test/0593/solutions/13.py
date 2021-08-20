(n, m) = list(map(int, input().split()))
ij = [list(map(int, input().split())) for i in range(m)]
ni = [0] * n
for i in range(m):
    maxi = 0
    num = 0
    for j in range(n):
        if ij[i][j] > maxi:
            maxi = ij[i][j]
            num = j
    ni[num] += 1
maxi = 0
num = 0
for i in range(n):
    if ni[i] > maxi:
        maxi = ni[i]
        num = i
print(num + 1)
