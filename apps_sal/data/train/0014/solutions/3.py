import math
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    c, d = list(map(int, input().split()))
    if min(c, d) + min(a, b) == max(a, b) and max(a, b) == max(c, d):
        print("Yes")
    else:
        print("No")
