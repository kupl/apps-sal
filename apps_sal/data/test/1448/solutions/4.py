n, d = [int(x) for x in input().split()]
for i in range(int(input())):
    x, y = [int(j) for j in input().split()]
    if (d <= x + y and x + y <= (n + n - d)) and (y <= x + d and y >= x - d):
        print("YES")
    else:
        print("NO")
