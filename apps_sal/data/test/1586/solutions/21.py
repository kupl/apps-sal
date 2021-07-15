import sys
N = int(input())
if N %2 !=0:
    print(0)
    return
else:
    sum = 0
    num = N
    num_tmp = num //5
    while num_tmp > 0:
        num_tmp = num // 5
        sum += num // 10
        num = num_tmp
print(sum)
