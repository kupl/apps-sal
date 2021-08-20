first_line = list(map(int, input().split(' ')))
number_moments = first_line[0]
x_val = first_line[1]
moments = []
for i in range(number_moments):
    moments.append(list(map(int, input().split(' '))))
current_time = 1
watched = 0
for m in moments:
    remaining = m[0] - current_time
    skippable = remaining // x_val
    current_time += x_val * skippable
    watched += m[1] - current_time + 1
    current_time = m[1] + 1
print(watched)
