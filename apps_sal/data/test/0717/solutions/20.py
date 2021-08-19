n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
curr = 0
for i in range(n):
    if curr < a[i][0]:
        curr = a[i][0]
    else:
        curr = a[i][0] + ((curr - a[i][0]) // a[i][1] + 1) * a[i][1]
print(curr)
