s = [[0] * 100 for k in range(100)]
k = 0
n = int(input())
s1 = [list(map(int, input().split())) for j in range(n)]
for i in range(len(s1)):
    for i1 in range(s1[i][0], s1[i][2] + 1):
        for i2 in range(s1[i][1], s1[i][3] + 1):
            k += 1
print(k)
