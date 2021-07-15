x = int(input())

ub = 10**9
lb = 0

while ub - lb > 1:
    mid = (lb + ub) // 2
    if mid*(mid+1)//2 >= x:
        ub = mid
    else:
        lb = mid
print(ub)
