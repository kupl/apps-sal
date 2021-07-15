w, h, x, y = map(int, input().split())

ans = w * h / 2

if x == w / 2 and y == h / 2:
    d = "1"
else:
    d = "0"
    
print(ans, d)
