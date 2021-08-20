def function(n, array):
    grid = [{} for i in range(n)]
    if n <= 2:
        print(n)
        return
    global_max = -10
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            diff = array[i] - array[j]
            max_val = 1
            if -diff in grid[j].keys():
                max_val = max(grid[j][-diff] + 1, max_val)
            if diff in grid[i].keys():
                max_val = max(max_val, grid[i][diff])
                grid[i][diff] = max_val
            else:
                grid[i][diff] = max_val
            global_max = max(global_max, max_val)
    print(global_max + 1)


n = int(input())
array = [int(x) for x in input().split()]
function(n, array)
