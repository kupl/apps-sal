h,w = list(map(int, input().split()))
ans = 10**10
if h%3 == 0 or w%3 == 0:
    print(0)
    return
    
for H in range(1, h + 1):
    a = H * w
    b = (h - H) * (w // 2)
    c = (h - H) * (w - w // 2)
    ans = min(ans, max(a,b,c) - min(a,b,c))

for W in range(1, w + 1):
    a = W * h
    b = (w - W) * (h // 2)
    c = (w - W) * (h - h // 2)
    ans = min(ans, max(a,b,c) - min(a,b,c))

if h > 3:
    ans = min(ans, w*((h+2)//3) - w*(h//3))

if w > 3:
    ans = min(ans, h*((w+2)//3) - h*(w//3))
    
print(ans)
