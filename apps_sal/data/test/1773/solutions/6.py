l = 0
lc = 0
r = 0
rc = 0
n = int(input())
arrl = []
arrr = []
for i in range(n):
    a, b = list(map(int, input().split()))
    if (a < 0):
        arrl.append((-a, b))
    else:
        arrr.append((a, b))
arrr.sort()
arrl.sort()
left = 0
right = 0
if (len(arrr) == len(arrl)):
    for i in range(min(len(arrr), len(arrl))):
        left += (arrr[i][1] + arrl[i][1])
elif (len(arrr) < len(arrl)):
    for i in range(min(len(arrr), len(arrl))):
        left += (arrr[i][1] + arrl[i][1])
    left += arrl[len(arrr)][1]
else:
    for i in range(min(len(arrr), len(arrl))):
        left += (arrr[i][1] + arrl[i][1])
    left += arrr[len(arrl)][1]

print(left)
