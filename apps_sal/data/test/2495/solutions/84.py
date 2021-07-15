n = int(input())
A = [int(i) for i in input().split()]
ct_1 = 0
ct_2 = 0
aa = 0

j = 1
for i in range(n):
    if (aa + A[i]) * j <= 0:
        ct_1 += abs(aa + A[i]) + 1
        aa = j
    else:
        aa += A[i]
    j *= -1

aa = 0
j = -1
for i in range(n):
    if (aa + A[i]) * j <= 0:
        ct_2 += abs(aa + A[i]) + 1
        aa = j
    else:
        aa += A[i]
    j *= -1

print((min(ct_1, ct_2)))

