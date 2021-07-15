A, B, C = list(map(int,input().split()))
sum_l = A + B + C
max_l = max(A, B, C)

dif = 3*max_l - sum_l
if dif % 2 == 0:
    print(dif // 2)
else:
    print((dif // 2) + 2)
