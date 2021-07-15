import sys

input = sys.stdin.readline
a, b, c, x, y= map(int, input().split())
ab = 2*c
count_x = 0
count_y = 0
buy_a = 0
buy_b = 0
buy_c = 0

if ab < a+b:
    min_count = min(x,y)
    count_x = min_count
    count_y = min_count
    buy_c = 2*min_count
    if x - count_x > 0:
        if ab > a:
            buy_a += x - count_x
        else:
            buy_c += 2 * (x - count_x)
    
    elif y - count_y > 0:
        if ab > b:
            buy_b += y - count_y
        else:
            buy_c += 2*(y - count_y)
else:
    min_count = min(x,y)
    if min_count == x:
        buy_a = min_count
        if ab > b:
            buy_b += y
        else:
            buy_c += 2 * y
    else:
        buy_b = min_count
        if ab > a:
            buy_a += x
        else:
            buy_c += 2 * x

print(buy_a * a + buy_b * b + buy_c * c)
