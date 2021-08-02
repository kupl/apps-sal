import sys
import copy

cases = sys.stdin.readline()
my_input = []
for line in sys.stdin.readlines():
    my_input.append(line.strip().split(" "))


my_dict = dict()
for line in my_input:
    arr = []
    for i in range(2, len(line)):
        arr.append(line[i])
    if (line[0] in my_dict):
        my_dict[line[0]].update(arr)
    else:
        my_dict[line[0]] = set(arr)

for x in my_dict:
    values = my_dict[x]
    final_values = copy.deepcopy(values)
    for a in values:
        for b in values:
            if(a.endswith(b) and a != b and b in final_values):
                final_values.remove(b)
    my_dict[x] = final_values

print(len(my_dict))
for x in my_dict:
    print(str(x) + " " + str(len(my_dict[x])) + " " + ' '.join(my_dict[x]))
