N = int(input())
C = list(input())
count = list()
W = 0
R = 0
for i in C:
    if i == 'R':
        R += 1
if R == 0:
    count.append(0)
for i in C:
    if i == 'W':
        W += 1
    else:
        R -= 1
    if W <= R:
        count.append(R)
    else:
        count.append(W)
print(min(count))
