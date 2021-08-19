import sys
(min_a_index, max_z_index) = (sys.maxsize, 0)
for (index, c) in enumerate(list(input())):
    if c == 'A' and index < min_a_index:
        min_a_index = index
    if c == 'Z' and index > max_z_index:
        max_z_index = index
print(max_z_index - min_a_index + 1)
