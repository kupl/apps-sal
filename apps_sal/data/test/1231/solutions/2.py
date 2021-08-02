a, b = list(map(int, input().split()))
if abs(a - b) <= 1 and (a, b) != (0, 0):
    print("YES")
else:
    print("NO")
