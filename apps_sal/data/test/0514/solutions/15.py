from math import ceil
t = int(input())
for i in range(t):
    n, d = map(int, input().split())
    for x in range(0, n):
        if x + ceil(d / (x + 1)) <= n:
            print("YES")
            break
    else:
        print("NO")
