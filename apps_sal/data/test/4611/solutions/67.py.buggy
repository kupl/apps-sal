n = int(input())
ti, xi, yi = (0, 0, 0)
for i in range(n):
    ti1, xi1, yi1 = list(map(int, input().split()))
    if abs(xi1 - xi) + abs(yi1 - yi) <= (ti1 - ti) and (abs(xi1 - xi) + abs(yi1 - yi)) % 2 == (ti1 - ti) % 2:
        xi = xi1
        yi = yi1
        ti = ti1
        continue
    else:
        print("No")
        return
print("Yes")
