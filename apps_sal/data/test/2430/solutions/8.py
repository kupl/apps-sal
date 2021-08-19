# problem 9
# Start 8:39
def seconds(l):
    time = 0
    h = 0
    for i in range(len(l) - 1):
        # Climb the tree
        if h < l[i]:
            time += l[i] - h
            h += l[i] - h

        # eat
        time += 1

        # get down to the height of th enext tree
        if h > l[i + 1]:
            time += h - l[i + 1]
            h -= h - l[i + 1]

        # jump to the next tree
        time += 1

    # the last tree
    # Climb the tree
    if h < l[-1]:
        time += l[-1] - h
        h += l[-1] - h
    # eat
    time += 1

    return time


m = int(input())
l = []
for i in range(m):
    l.append(int(input()))
print(seconds(l))

# End 8:56
# Total 17 min
