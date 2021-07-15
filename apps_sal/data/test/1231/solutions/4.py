a, b = [int(x) for x in input().split()]
if a == 0 and b == 0:
    print("NO")
elif abs(a - b) <= 1:
    print("YES")
else:
    print("NO")

