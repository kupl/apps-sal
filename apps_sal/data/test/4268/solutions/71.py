import math
N, D = map(int, input().split())
X = [list(map(int, input().split())) for i in range(N)]

seisu_count = 0
for l in range(N):

    for r in range(l + 1, N):
        total = 0
        for z in range(D):
            y_z = abs(X[l][z] - X[r][z])
            y_z_2 = y_z * y_z
            total += y_z_2

        sqr_total = math.sqrt(total)
        if sqr_total.is_integer():
            seisu_count += 1

print(seisu_count)
