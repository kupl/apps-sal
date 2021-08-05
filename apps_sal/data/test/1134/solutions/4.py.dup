n = int(input())
m = input().split(' ')
j = 0
mark = [1]
for i in range(1, len(m)):
    tmp = max(mark[i - 1], int(m[i]) + 1)
    mark.append(tmp)

j += mark[len(m) - 1] - int(m[len(m) - 1]) - 1
for i in range(len(m) - 2, -1, -1):
    if mark[i] < mark[i + 1] - 1:
        mark[i] = mark[i + 1] - 1
    j += mark[i] - int(m[i]) - 1
print(j)
