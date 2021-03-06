inputs = [int(x) for x in input().split()]
mins = inputs[1]
book_times = [int(x) for x in input().split()]
current_max = -1
current_time = 0
start_idx = 0
end_idx = -1
for i in range(len(book_times)):
    t = book_times[i]
    if t + current_time > mins:
        current_max = end_idx - start_idx if end_idx - start_idx > current_max else current_max
        while start_idx <= end_idx and t + current_time > mins:
            current_time -= book_times[start_idx]
            start_idx += 1
    if t + current_time <= mins:
        current_time += t
    else:
        current_time = 0
        start_idx = i + 1
    end_idx = i
current_max = end_idx - start_idx if end_idx - start_idx > current_max else current_max
print(current_max + 1)
