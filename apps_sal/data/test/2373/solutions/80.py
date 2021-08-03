n = int(input())
p = list(map(int, input().split()))
cnt_1 = 0
cnt_2 = 0
TF = False
for i in range(n):
    if (i + 1) == p[i]:
        if TF:
            TF = False
            cnt_2 += 1
            cnt_1 -= 1
        else:
            TF = True
            cnt_1 += 1
    else:
        TF = False
print(cnt_1 + cnt_2)
