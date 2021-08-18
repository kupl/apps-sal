n = int(input())

sum_x = 0
sum_y = 0

odd_even = 0
odd_odd = 0
even_odd = 0
even_even = 0

for i in range(n):
    x, y = map(int, input().split())
    sum_x += x
    sum_y += y
    if x % 2 == 0 and y % 2 == 0:
        odd_odd += 1
    elif x % 2 == 0 and y % 2 == 1:
        odd_even += 1
    elif x % 2 == 1 and y % 2 == 0:
        even_odd += 1
    else:
        even_even += 1

if sum_x % 2 == 0 and sum_y % 2 == 0:
    print(0)
elif sum_x % 2 == 0 and sum_y % 2 == 1:
    print(-1)
elif sum_x % 2 == 1 and sum_y % 2 == 0:
    print(-1)
else:
    if even_odd >= 1 or odd_even >= 1:
        print(1)
    else:
        print(-1)
