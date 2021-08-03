import sys
import filecmp

FILE_IO = False

if FILE_IO:
    input_stream = open('input_test.txt')
    sys.stdout = open('current_output.txt', 'w')
else:
    input_stream = sys.stdin

input_line = input_stream.readline().split()

array_len = int(input_line[0])
num_of_days = int(input_line[1])
stripe_len = int(input_line[2])

input_line = input_stream.readline().split()

input_list = []
for i in range(0, array_len):
    input_list.append(int(input_line[i]))

min_input = min(input_list)
max_input = max(input_list)
left = min_input
right = max_input + num_of_days
current_solution = left
while left <= right:
    mid = int(right + (left - right) / 2)

    number_of_additions_list = [0 for _ in input_list]
    needed_steps = 0
    for index, current_flower_state in enumerate(input_list):
        needed_addtion = 0
        if index > 0:
            prv_elem = number_of_additions_list[index - 1]
        else:
            prv_elem = 0
        current_addition = prv_elem + number_of_additions_list[index]
        if current_flower_state < mid:

            state_with_prev_addition = (current_flower_state + current_addition)

            if state_with_prev_addition < mid:
                needed_addtion = mid - state_with_prev_addition
                needed_steps += needed_addtion

                if (index + stripe_len < len(input_list)):
                    number_of_additions_list[index + stripe_len] = (needed_addtion * -1)

        number_of_additions_list[index] = current_addition + needed_addtion
    if needed_steps > num_of_days:
        right = mid - 1
    else:
        if current_solution < mid:
            current_solution = mid
        left = mid + 1
print(current_solution)


if FILE_IO:
    assert filecmp.cmp('current_output.txt', 'expected_output.txt', shallow=False) == True
