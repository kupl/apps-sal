n, k, p, x, y = map(int, input().split())
written = sorted([int(x) for x in input().split()])

# very smart
if sum(written) + (n - k) > x:
    print(-1)
    return

answer = []
for i in range(n - k):

    median_index = (len(written)) // 2
    if len(written) % 2 == 0:
        try:
            test = written[median_index - 1]
        except IndexError:
            test = 0

        if test < y:
            written.append(y)
            answer.append(y)
        else:
            written.append(1)
            answer.append(1)
    elif written[median_index] < y:
        written.append(y)
        answer.append(y)
    else:
        written.append(1)
        answer.append(1)
    written.sort()


median_index = len(written) // 2
if sum(written) > x or written[median_index] < y:
    print(-1)
    return

print(' '.join(str(x) for x in answer))
