import sys
import itertools

inputs = sys.stdin.read().split()
len_string = int(inputs[0])
desired_size = int(inputs[1])
string = inputs[2]


def val_of_letter(char): return ord(char) - ord("a")


num_subsequences = [1]
num_subsequences_so_far = [0] * len_string
last_num_subsequences_so_far = [0] * len_string
num_subsequences_for_this_letter_so_far = [0] * 26

last_num_subsequences_so_far[len_string - 1] = 1
num_subsequences_for_this_letter_so_far[val_of_letter(string[-1])] = 1

for i in range(len_string - 2, -1, -1):
    last_num_subsequences_so_far[i] = \
        last_num_subsequences_so_far[i + 1]
    if num_subsequences_for_this_letter_so_far[val_of_letter(string[i])] == 0:
        last_num_subsequences_so_far[i] += 1
        num_subsequences_for_this_letter_so_far[val_of_letter(string[i])] = 1
num_subsequences.append(last_num_subsequences_so_far[0])

for length in range(2, len_string + 1):
    for i in range(26):
        num_subsequences_for_this_letter_so_far[i] = 0

    num_subsequences_so_far[len_string - 1] = 0
    for i in range(len_string - 2, -1, -1):
        num_subsequences_so_far[i] = \
            num_subsequences_so_far[i + 1] + \
            last_num_subsequences_so_far[i + 1] - \
            num_subsequences_for_this_letter_so_far[val_of_letter(string[i])]
        num_subsequences_for_this_letter_so_far[val_of_letter(string[i])] = \
            last_num_subsequences_so_far[i + 1]

    num_subsequences.append(num_subsequences_so_far[0])
    for i in range(len_string):
        last_num_subsequences_so_far[i] = num_subsequences_so_far[i]

size = 0
cost = 0
for i in range(len_string, -1, -1):
    cur_size = num_subsequences[i]
    if size + cur_size >= desired_size:
        cost += (desired_size - size) * (len_string - i)
        size = desired_size
        break
    cost += cur_size * (len_string - i)
    size += cur_size

if size >= desired_size:
    sys.stdout.write(str(cost) + "\n")
else:
    sys.stdout.write("-1\n")
