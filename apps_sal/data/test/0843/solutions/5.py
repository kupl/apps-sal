n = int(input())
cells = input()
lengths = list(map(int, input().split()))
visited = set()
i = 0
while i not in visited and i < n and (i > -1):
    visited.add(i)
    if cells[i] == '>':
        i += lengths[i]
    else:
        i -= lengths[i]
if i < n and i >= 0:
    print('INFINITE')
else:
    print('FINITE')
