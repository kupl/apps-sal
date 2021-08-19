n = int(input())
instructions = list(zip(input(), [int(i) for i in input().split()]))
used = set()
pos = 0
while True:
    if pos < 0 or pos >= n:
        print('FINITE')
        break
    if pos in used:
        print('INFINITE')
        break
    used.add(pos)
    (direct, length) = instructions[pos]
    if direct == '>':
        pos += length
    else:
        pos -= length
