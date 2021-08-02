n, k = list(map(int, input().split()))

bact = list(map(int, input().split()))
bact.sort()
res = 0
live = 1
for i in range(n - 1):
    if bact[i + 1] == bact[i]:  # cannot consume
        live += 1
    elif bact[i + 1] - bact[i] > k:  # all unconsumed survived
        res += live
        live = 1
    else:
        live = 1  # current is alive, others eaten

res += live

print(res)
