n, k = list(map(int, input().split()))
lines = [[ch for ch in input()] + ['\n'] for i in range(n)]
queue = [[], [], []]
count = 0

for i in range(n):
    for seat in range(12):
        if lines[i][seat] == '.':
            queue[(lines[i][seat - 1] == 'S') + (lines[i][seat + 1] == 'S')].append([i, seat])
        elif lines[i][seat] == 'S':
            count += (lines[i][seat - 1] > 'A') + (lines[i][seat + 1] > 'A')

while k:
    if queue[0]: seat = queue[0].pop()
    elif queue[1]:
        seat = queue[1].pop()
        count += 1
    else:
        seat = queue[2].pop()
        count += 2

    lines[seat[0]][seat[1]] = 'x'
    k -= 1

print(count)
print(''.join([''.join(line) for line in lines]))
