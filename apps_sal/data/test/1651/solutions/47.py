S, P = list(map(int, input().split()))
v = S**2 - 4*P
if v < 0:
    print("No")
elif v == 0:
    print("Yes")
else:
    left = 1
    right = v
    while right - left > 1:
        mid = (left+right)//2
        if mid**2 > v:
            right = mid
        else:
            left = mid
    if left**2 == v:
        print("Yes")
    else:
        print("No")

