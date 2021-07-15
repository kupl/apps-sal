n = int(input())
index = 1
memory = set()
counter = 0
segments = [[0, 0]]
for number in input().split():
    if number not in memory:
        memory.add(number)
    else:
        counter += 1
        segments.append([segments[-1][1] + 1, index])
        memory = set()
    index += 1
segments[-1][1] = n
if counter != 0:
    print(counter)
    segments.remove([0, 0])
    print('\n'.join('{0} {1}'.format(p, q) for (p, q) in segments))
else:
    print(-1)
