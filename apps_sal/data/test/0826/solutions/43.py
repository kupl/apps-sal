n = int(input())

left = 0
right = n+1 
while right - left > 1:
    m = (right + left) // 2
    if m * (m+1)//2 <= (n+1):
        left = m
    else:
        right = m


print(n+1-left)
