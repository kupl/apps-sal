def in_interval(w, x, y, z):
    if (w > y and w < z) or (x > y and x < z):
        return True
    else:
        return False


def step_through(a, b, c, d, temp):
    x = None
    for interval in temp:
        e = int(interval[0])
        f = int(interval[1])
        if in_interval(a, b, c, d):
            return True
        elif in_interval(a, b, e, f):
            x = interval
            temp.remove(interval)
            if step_through(e, f, c, d, temp):
                return True
    if(x != None):
        temp.append(x)
    return False


n = int(input())
set_of_intervals = []
for i in range(n):
    line = input().split()

    if line[0] == "1":
        set_of_intervals.append([line[1], line[2]])
    else:
        a = int(set_of_intervals[int(line[1]) - 1][0])
        b = int(set_of_intervals[int(line[1]) - 1][1])
        c = int(set_of_intervals[int(line[2]) - 1][0])
        d = int(set_of_intervals[int(line[2]) - 1][1])

        temp = set_of_intervals[:]
        temp.pop(int(line[1]) - 1)
        if(step_through(a, b, c, d, temp)):
            print("YES")
        else:
            print("NO")
