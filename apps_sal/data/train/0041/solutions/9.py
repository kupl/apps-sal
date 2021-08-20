t = int(input())
for i in range(t):
    (n, k) = map(int, input().split())
    (*s,) = input()
    operations = []
    best = (['('] + [')']) * (k - 1) + (['('] * (n // 2 - k + 1) + [')'] * (n // 2 - k + 1))
    for startx_pos in range((k - 1) * 2):
        try:
            if s[startx_pos - 1] == ')' or startx_pos == 0:
                end_pos = s.index('(', startx_pos)
            else:
                end_pos = s.index(')', startx_pos)
        except ValueError:
            continue
        if startx_pos == end_pos:
            continue
        if startx_pos == 0:
            s = s[:startx_pos] + s[end_pos::-1] + s[end_pos + 1:]
        else:
            s = s[:startx_pos] + s[end_pos:startx_pos - 1:-1] + s[end_pos + 1:]
        operations.append(f'{startx_pos + 1} {end_pos + 1}')
    for startx_pos in range((k - 1) * 2, (k - 1) * 2 + (n // 2 - k + 1)):
        try:
            end_pos = s.index('(', startx_pos)
        except ValueError:
            continue
        if startx_pos == end_pos:
            continue
        if startx_pos == 0:
            s = s[:startx_pos] + s[end_pos::-1] + s[end_pos + 1:]
        else:
            s = s[:startx_pos] + s[end_pos:startx_pos - 1:-1] + s[end_pos + 1:]
        operations.append(f'{startx_pos + 1} {end_pos + 1}')
    print(len(operations))
    if len(operations):
        print(*operations, sep='\n')
