line_length = int(input())
directions = input()
distances = [int(distance) for distance in input().split()]
visited_cells = set()
current_cell = 0
while 0 <= current_cell < line_length:
    if current_cell in visited_cells:
        break
    else:
        visited_cells.add(current_cell)
        if directions[current_cell] == '>':
            current_cell += distances[current_cell]
        else:
            current_cell -= distances[current_cell]
if 0 <= current_cell < line_length:
    print("INFINITE")
else:
    print("FINITE")

