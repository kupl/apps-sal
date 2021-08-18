import math

A, B, C, D = map(int, input().split(' '))

num_C_baisu = B // C - (A - 1) // C

num_D_baisu = B // D - (A - 1) // D

CD = int(C * D / math.gcd(C, D))

num_CD_baisu = B // CD - (A - 1) // CD

baisu_num = num_C_baisu + num_D_baisu - num_CD_baisu

print(B - A + 1 - baisu_num)
