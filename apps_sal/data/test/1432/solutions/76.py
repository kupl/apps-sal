N = int(input())
lsA = list(map(int, input().split()))
x1_2 = 0
for i in range(N):
    if i % 2 == 0:
        x1_2 += lsA[i]
    else:
        x1_2 -= lsA[i]
x1 = x1_2 // 2
lsx = [x1]
for i in range(N):
    lsx.append(lsA[i] - lsx[i])
lsx2 = [str(2 * lsx[i]) for i in range(N)]
print(' '.join(lsx2))
