import sys

cases = sys.stdin.readline()
my_list = [int(a) for a in sys.stdin.readline().split(" ")]

max_val_a = my_list[0]
max_val_b = 0

my_counts = dict()
for x in my_list:
    my_counts[x] = 0

my_counts[max_val_a] = -1

for x in my_list:
    if(x > max_val_a):
        my_counts[x] = my_counts[x] - 1
        max_val_a, max_val_b = x, max_val_a
    elif (x < max_val_a and x > max_val_b):
        my_counts[max_val_a] = my_counts[max_val_a] + 1
        max_val_b = x

highest = max(my_counts.values())
print(min([k for k, v in my_counts.items() if v == highest]))
