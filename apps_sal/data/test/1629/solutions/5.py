n = [int(num) for num in input().split()]
x = [int(num) for num in input().split()]
i = n[1] - 1
j = (i - 1) % n[0]
while j != n[1] - 1:
    if x[j] < x[i]:
        i = j
    j = (j - 1) % n[0]
p = x[i]
j = (n[1] - i - 1) % n[0]
if p != x[n[1] - 1]:
    x[i] = p * n[0] + j
    i = i + 1
else:
    x[n[1] - 1] = p * n[0]
    j = 0
    i = n[1]
t = i - 1
while True:
    if j != 0:
        j = j - 1
        x[i % n[0]] = x[i % n[0]] - 1 - p
    else:
        x[i % n[0]] = x[i % n[0]] - p
    if (i + 1) % n[0] == t:
        break
    else:
        i = (i + 1)
for i in x:
    print(i, end=' ')
