t = int(input())
for i in range(t):
    r, g, b = list(map(int, input().split()))
    mx = max(r, g, b)
    s = r + g + b - mx + 1
    if s < mx:
        print("No")
    else:
        print("Yes")
