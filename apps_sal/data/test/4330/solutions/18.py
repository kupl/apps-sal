a,b = [int(v) for v in input().split()]
if abs(a-b) % 2 == 0:
    print((int((max(a,b)+min(a,b))/2)))
else:
    print("IMPOSSIBLE")

