n, k = list(map(int, input().split()))
dList = list(map(int, input().split()))
maxD = 0
d = {}
for i in dList:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
    if d[i] > maxD:
        maxD = d[i]
amount = 0
dis = ((maxD - 1) // k + 1) * k
for i in list(d.values()):
    amount += dis - i
print(amount)

