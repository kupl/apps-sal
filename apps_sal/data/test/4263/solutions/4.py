str_list = list(input())

count = 0
max_count = 0
for char in str_list:
    if char == 'A' or char == 'C' or char == 'G' or char == 'T':
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0
if count > max_count:
    max_count = count
print(max_count)
