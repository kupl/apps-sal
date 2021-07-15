X, N = map(int, input().split())
p = list(map(int, input().split()))

if not X in p:
    print(X)
    return

left = -200
for a in range(X-1, -1, -1):
    if not a in p:
        left = a 
        break

right = 200
for a in range(X + 1, 102):
    if not a in p:
        right = a
        break 

if X - left > right - X:
    print(right)
else:
    print(left)
