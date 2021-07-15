total_square, total_toll_gate, current_square = map(int, input().split())
toll_gate_square = list(map(int, input().split()))
route1 = 0
route2 = 0
for i in range(total_toll_gate):
    if toll_gate_square[i] < current_square:
        route1 += 1
    else:
        route2 += 1
print(min(route1, route2))
