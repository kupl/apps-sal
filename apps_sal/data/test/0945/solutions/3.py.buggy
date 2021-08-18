n = int(input())
a = [int(x) for x in input().split()]
x = []
for i in range(n - 1):
    x.append(sorted([a[i], a[i + 1]]))
# print(x)
for i in range(n - 1):
    for j in range(i + 2, n - 1):
        if (x[i][0] > x[j][0] and x[i][0] < x[j][1] and (x[i][1] > x[j][1] or x[i][1] < x[j][0])) or (x[i][1] > x[j][0] and x[i][1] < x[j][1] and (x[i][0] > x[j][1] or x[i][0] < x[j][0])):
            print('yes')
            return
print('no')
