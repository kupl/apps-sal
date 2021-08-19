n = int(input())
pos = []
neg = []
for i in range(n):
    (a, b) = list(map(int, input().split()))
    if a < 0:
        neg.append((a, b))
    else:
        pos.append((a, b))
neg = sorted(neg, reverse=True)
pos.sort()
no1 = 0
no2 = 0
temp1 = list(neg)
temp2 = list(pos)
i = 0
while True:
    if i == 0:
        if len(temp1) == 0:
            break
        (x, cur) = temp1[0]
        i = 1
        no1 += cur
        temp1.pop(0)
    if i == 1:
        if len(temp2) == 0:
            break
        (x, cur) = temp2[0]
        i = 0
        no1 += cur
        temp2.pop(0)
i = 0
while True:
    if i == 0:
        if len(pos) == 0:
            break
        (x, cur) = pos[0]
        i = 1
        no2 += cur
        pos.pop(0)
    if i == 1:
        if len(neg) == 0:
            break
        (x, cur) = neg[0]
        i = 0
        no2 += cur
        neg.pop(0)
print(max(no1, no2))
