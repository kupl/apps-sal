a = [len(input()) - 2 for i in range(4)]
cnt = 0
res = 2
for i in range(4):
    flag1 = True
    flag2 = True
    for j in range(4):
        if j != i:
            if a[i] < a[j] * 2:
                flag1 = False
            if a[i] * 2 > a[j]:
                flag2 = False
    if flag1 or flag2:
        cnt += 1
        res = i
if cnt == 1:
    print(["A", "B", "C", "D"][res])
else:
    print("C")
