n, k = list(map(int, input().split()))

bact = list(map(int, input().split()))
bact.sort()
res = 0
live = 1
for i in range(n - 1):
    if bact[i + 1] == bact[i]:
        live += 1
    elif bact[i + 1] - bact[i] > k:
        res += live
        live = 1
    else:
        live = 1

res += live

print(res)
