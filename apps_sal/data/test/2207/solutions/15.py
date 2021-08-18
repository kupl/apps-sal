import sys
with sys.stdin as f:
    input_list = list(f)
for i, line in enumerate(input_list):
    if i == 0:
        R = int(line.split(" ")[0])
    else:
        if i == R:
            nb_walls = len(list(filter(lambda x: len(x) > 0, line.strip().split('.'))))
            print(nb_walls)
