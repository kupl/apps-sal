n = int(input())
summ_x = 0
summ_y = 0
for i in range(2 * n):
    a, b = map(int, input().split())
    summ_x += a
    summ_y += b
print(summ_x // n, summ_y // n)
