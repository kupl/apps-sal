n = int(input())
sher = input()
mor = input()
morD = [0] * 10
for i in mor:
    morD[int(i)] += 1
ans1 = 0
for i in sher:
    k = int(i)
    while k < 10 and morD[k] == 0:
        k += 1
    if k == 10:
        ans1 += 1
        k = 0
        while morD[k] == 0:
            k += 1
    morD[k] -= 1
print(ans1)
morD = [0] * 10
for i in mor:
    morD[int(i)] += 1
ans2 = 0
for i in sher:
    k = int(i)
    if k == 9:
        k = 0
        while morD[k] == 0:
            k += 1
    else:
        k += 1
        while k < 10 and morD[k] == 0:
            k += 1
        if k == 10:
            k = 0
            while morD[k] == 0:
                k += 1
        else:
            ans2 += 1
    morD[k] -= 1
print(ans2)

