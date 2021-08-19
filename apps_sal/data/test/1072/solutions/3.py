line = input().split()
n = int(line[0])
m = int(line[1])
data = []
for i in range(n):
    data.append(input())
x = [1 for i in range(n)]
delete = 0
for i in range(m):
    dum = [1 for j in range(n)]
    status = 1
    for j in range(1, n):
        if data[j][i] > data[j - 1][i]:
            dum[j] = 0
        elif data[j][i] == data[j - 1][i]:
            dum[j] = 1
        elif x[j] == 1:
            delete += 1
            status = 0
            break
    if status == 1:
        for j in range(len(dum)):
            if dum[j] == 0:
                x[j] = 0
print(delete)
