n, m, x = list(map(int, input().split()))
squares = list(map(int, input().split()))

left_cost = 0
right_cost = 0
for square in squares:
    if square < x:
        left_cost = left_cost + 1
    else:
        right_cost = right_cost + 1

print((min(right_cost, left_cost)))
