t = int(input())
while t:
    r, g, b = map(int, input().split())
    x = max(r, g, b)
    y = r + g + b - max(r, g, b)
    if(x - y <= 1):
        print("Yes")
    else:
        print("No")
    t -= 1
