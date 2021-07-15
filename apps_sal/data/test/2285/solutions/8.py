import re

n = int(input())
for i in range(n):
    s = input().strip()
    group_count = s.count(':') + 1
    if group_count < 8:
        s = re.sub('::', ':' + (9 - group_count) * '0000:', s)
    elif group_count == 9:
        s = re.sub('::', ':', s)
    groups = s.split(':')
    for i, group in enumerate(groups):
        if len(group) < 4:
            groups[i] = (4 - len(group)) * '0' + group
    print(':'.join(groups))

