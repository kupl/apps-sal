N = int(input())
lsA = list(map(int, input().split()))
lsB = list(map(int, input().split()))
stA = sum(lsA)
for i in range(N):
    if lsA[i] >= lsB[i]:
        lsA[i] -= lsB[i]
        lsB[i] = 0
    else:
        lsB[i] -= lsA[i]
        lsA[i] = 0
        if lsA[i + 1] >= lsB[i]:
            lsA[i + 1] -= lsB[i]
            lsB[i] = 0
        else:
            lsA[i + 1] = 0
            lsB[i] -= lsA[i + 1]
enA = sum(lsA)
print(stA - enA)
