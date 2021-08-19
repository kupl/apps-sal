c1 = {}
c2 = {}
count = 0
n = int(input())
for i in range(n):
    (a, b) = input().split(' ')
    if a in c1:
        c1[a] += 1
    else:
        c1[a] = 1
    if b in c2:
        c2[b] += 1
    else:
        c2[b] = 1
for i in c2:
    if i in c1:
        count += c1[i] * c2[i]
print(count)
