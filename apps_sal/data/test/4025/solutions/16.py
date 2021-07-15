a, b, c = [int(elem) for elem in input().split()]

num_weeks = min(a // 3, b // 2, c // 2)
a -= 3 * num_weeks
b -= 2 * num_weeks
c -= 2 * num_weeks

# rest_rations = [a, b, c]
max_num_additional_days = 0

what_to_eat = [0, 0, 1, 2, 0, 2, 1]
for start in range(7):
    rest_rations = [a, b, c]
    num_additional_days = 0
    for i in range(start, start + 7):
        day = i % 7
        food_to_eat_today = what_to_eat[day]
        if rest_rations[food_to_eat_today] == 0:
            break
        rest_rations[food_to_eat_today] -= 1
        num_additional_days += 1
    max_num_additional_days = max(max_num_additional_days, num_additional_days)

print(max_num_additional_days + num_weeks * 7)

