n, s = list(map(int, input().split()))
mx = -1
for i in range(n):
    x, y = list(map(int, input().split()))
    if x < s or (x == s and y == 0):
        mx = max(mx, 100 - (y or 100))
print(mx) 

