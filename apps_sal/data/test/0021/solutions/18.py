n = int(input())
a = [int(x) for x in input().split()]
pos1 = 0
pos2 = 0
for i in range(n):
    if (a[i] == 1 or a[i] == n):
        pos1 = i
        break

for i in range(pos1 + 1, n):
    if (a[i] == 1 or a[i] == n):
        pos2 = i
        break

print(pos2 - pos1 + max(n - pos2 - 1, pos1))
