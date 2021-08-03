a = int(input())
l = [int(i)for i in input().split()]
x = min(l)
id = 0
for i in l:
    if i == x:
        break
    id += 1
d = 1000000
for j in range(id + 1, len(l)):
    if l[j] == x:
        d = min(d, j - id)
        id = j
print(d)
