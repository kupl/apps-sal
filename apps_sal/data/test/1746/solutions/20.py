n = int(input())
l = [0] * n

for i in range(1, n):
    l[i] = int(input()) - 1

leaves = [1] * n
leaves[0] = 0

for i in range(n):
    for j in range(i, n - 1):
        if l[j] == i:
            leaves[i] = 0

spruce = 'Yes'

for i in range(n):
    if leaves[i] == 0:
        count = 0
        for j in range(i, n):
            if l[j] == i and leaves[j]:
                count += 1
        if count < 3:
            spruce = 'No'

print(spruce)
