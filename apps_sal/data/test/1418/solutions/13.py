n = int(input())
l = [0] * (n + 1)
great = 0
for i in range(2, n + 1):
    if l[i] == 0:
        great += 1
        for j in range(i, n + 1, i):
            l[j] = great
print(*l[2:])
