n = int(input())
curr_p = 1000
curr_meat = 0
coast = 0
for i in range(n):
    (a, p) = map(int, input().split())
    if p < curr_p:
        coast += curr_p * curr_meat
        curr_p = p
        curr_meat = a
    else:
        curr_meat += a
coast += curr_p * curr_meat
print(coast)
