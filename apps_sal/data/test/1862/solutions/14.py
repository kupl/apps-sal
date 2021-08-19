import sys
a = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
table = set([])
lenTabel = 0
for sock in arr:
    if sock in table:
        table.remove(sock)
    else:
        table.add(sock)
        lenTabel = len(table) if len(table) > lenTabel else lenTabel
print(lenTabel)
