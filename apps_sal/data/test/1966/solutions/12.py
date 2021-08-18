
n = int(input())
a = [[[0 for j in range(n)] for i in range(n)] for k in range(4)]
in1 = [[0, 0] for i in range(4)]

for k in range(4):
    for i in range(n):
        s = input()
        for j in range(n):
            a[k][i][j] = int(s[j])
            if(int(s[j]) == (i + j) % 2):
                in1[k][1] += 1
    in1[k][0] = n * n - in1[k][1]
    if(k != 3):
        s = input()
min1 = 10000000000

min1 = min(min1, in1[0][0] + in1[1][0] + in1[2][1] + in1[3][1])
min1 = min(min1, in1[0][0] + in1[1][1] + in1[2][0] + in1[3][1])
min1 = min(min1, in1[0][0] + in1[1][1] + in1[2][1] + in1[3][0])
min1 = min(min1, in1[0][1] + in1[1][1] + in1[2][0] + in1[3][0])
min1 = min(min1, in1[0][1] + in1[1][0] + in1[2][1] + in1[3][0])
min1 = min(min1, in1[0][1] + in1[1][0] + in1[2][0] + in1[3][1])
print(min1)
