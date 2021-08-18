import sys
n, k, m = map(int, input().split())
A = list(map(int, input().split()))
sum1 = sum(A)
gou = n * m
if gou <= sum1:
    print("0")
    return
if gou > sum1:
    if gou - sum1 > k:
        print("-1")
        return
    print(gou - sum1)
