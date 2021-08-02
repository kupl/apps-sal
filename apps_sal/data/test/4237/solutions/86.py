import math

A, B, C, D = map(int, input().split(' '))

num_C_baisu = B // C - (A - 1) // C  # (math.ceil(A/C) - 1)

num_D_baisu = B // D - (A - 1) // D  # (math.ceil(A/D) - 1)

CD = int(C * D / math.gcd(C, D))

num_CD_baisu = B // CD - (A - 1) // CD  # (math.ceil(A/CD) - 1)

baisu_num = num_C_baisu + num_D_baisu - num_CD_baisu

print(B - A + 1 - baisu_num)
