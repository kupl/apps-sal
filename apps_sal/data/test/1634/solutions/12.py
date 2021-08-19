import sys
line_id = 0
for line in sys.stdin:
    line_id = line_id + 1
    line_data = line.split()
    if line_id <= 2:
        if line_id == 1:
            c1 = int(line_data[0])
            c2 = int(line_data[1])
            c3 = int(line_data[2])
            c4 = int(line_data[3])
        else:
            cnt_bus = int(line_data[0])
            cnt_tro = int(line_data[1])
    elif line_id == 3:
        cnt_bus_took = [0]
        for data_str in line_data:
            cnt_bus_took.append(int(data_str))
    else:
        cnt_tro_took = [0]
        for data_str in line_data:
            cnt_tro_took.append(int(data_str))
cost_bus = 0
for bus_id in range(cnt_bus + 1):
    cost_bus = cost_bus + min(c1 * cnt_bus_took[bus_id], c2)
cost_bus = min(c3, cost_bus)
cost_tro = 0
for tro_id in range(cnt_tro + 1):
    cost_tro = cost_tro + min(c1 * cnt_tro_took[tro_id], c2)
cost_tro = min(c3, cost_tro)
cost_all = min(c4, cost_bus + cost_tro)
print(cost_all)
