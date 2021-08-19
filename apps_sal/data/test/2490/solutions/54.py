N = list(input())
N = N[::-1]
N_int = [int(i) for i in N]
N_int.append(0)
maisu = 0
keta = False
for i in range(len(N_int) - 1):
    if keta == True:
        N_int[i] += 1
    if N_int[i] < 5:
        maisu += N_int[i]
        keta = False
    elif N_int[i] == 5:
        if N_int[i + 1] > 4:
            keta = True
            maisu += 10 - N_int[i]
        else:
            keta = False
            maisu += N_int[i]
    else:
        keta = True
        maisu += 10 - N_int[i]
if keta == True:
    maisu += 1
print(maisu)
