import math
t = int(input())
for i in range(t):
    n, d = map(int, input().split())
    flag = 0
    for j in range(int(d**(0.5)) + 1):
        if math.ceil(d / (j + 1) + j) <= n:
            print("YES")
            flag = 1
            break
    if not flag:
        print("NO")
