n = int(input())
ps = list(map(lambda x: int(x)-1, input().split()))

sum = 0
maxest_pipe = 0
max_pipe = 0

free_points = set(range(n))
free_points.remove(0)
start_point = 0
current_point = 0
steps = 0
while True:
    steps += 1
    next_point = ps[current_point]
    if next_point in free_points:
        free_points.remove(next_point)
    if next_point == start_point:

        sum += steps * steps
        if steps > maxest_pipe:
            max_pipe = maxest_pipe
            maxest_pipe = steps
        elif steps > max_pipe:
            max_pipe = steps
        steps = 0
        if len(free_points) > 0:
            current_point = free_points.pop()
            start_point = current_point
        else:
            break
    else:
        current_point = next_point

print(sum - max_pipe*max_pipe - maxest_pipe*maxest_pipe + (max_pipe+maxest_pipe)*(max_pipe+maxest_pipe))
