from collections import OrderedDict

num_list = [n for n in range(0, 10)]
n = int(input())
char_priority_dict = {}
zero_is_permitted = {}
inputs = []
for c in 'abcdefghij':
    char_priority_dict[c] = 0
    zero_is_permitted[c] = True

for i in range(n):
    s = input()
    inputs.append(s)
    zero_is_permitted[s[0]] = False
    reversed_s = s[::-1]
    for (j, c) in enumerate(reversed_s):
        char_priority_dict[c] += 10 ** j

char_priority_dict = OrderedDict(sorted(char_priority_dict.items(), key=lambda x: x[1], reverse=True))
char_num_dict = {}

for char in char_priority_dict.keys():
    if 0 in num_list:
        if zero_is_permitted[char]:
            char_num_dict[char] = 0
            num_list.remove(0)
        else:
            char_num_dict[char] = num_list[1]
            num_list.remove(num_list[1])
    else:
        char_num_dict[char] = num_list[0]
        num_list.remove(num_list[0])

keys = ''.join(list(char_num_dict.keys()))
values = ''.join(list(map(str, char_num_dict.values())))
restored_values = []
for s in inputs:
    restored_values.append(int(s.translate(s.maketrans(keys, values))))

print(sum(restored_values))
