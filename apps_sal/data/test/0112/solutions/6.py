n = int(input())
data = [[0] * 6 for i in range(n)]
for i in range(n):
    data[i] = list(map(int, input().split()))
mb = set()
for i in range(n):
    for j in range(6):
        mb.add(data[i][j])
for i in range(n):
    for j in range(n):
        for k in range(6):
            for k2 in range(6):
                if(i != j):
                    mb.add(data[i][k] * 10 + data[j][k2])
                    mb.add(data[i][k] + data[j][k2] * 10)
if (n == 3):
    for k1 in range(6):
        for k2 in range(6):
            for k3 in range(6):
                mb.add(data[0][k] * 100 + data[1][k2] * 10 + data[2][k3])
                mb.add(data[0][k] * 100 + data[1][k2] + data[2][k3] * 10)
                mb.add(data[0][k] * 10 + data[1][k2] * 100 + data[2][k3])
                mb.add(data[0][k] + data[1][k2] * 100 + data[2][k3] * 10)
                mb.add(data[0][k] * 10 + data[1][k2] + data[2][k3] * 100)
                mb.add(data[0][k] + data[1][k2] * 10 + data[2][k3] * 100)
i = 1
while i in mb:
    i += 1
print(i - 1)
