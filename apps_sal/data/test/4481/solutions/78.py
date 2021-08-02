n = int(input())
count_dict = {}
for i in range(n):
    i = input()
    if i in count_dict.keys():
        count_dict[i] += 1
    else:
        count_dict[i] = 0
max_value = max(count_dict.values())
for key, value in sorted(count_dict.items()):
    if value == max_value:
        print(key)
