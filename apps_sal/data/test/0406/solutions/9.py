n = int(input())
lst = []
lst.extend(list(map(int, input().split())))
tarea = 0
lst.sort()
lst = lst[::-1]
lst.append(0)
i = 0
mark = 0
ar = []
while i != n:
    if lst[i] - lst[i + 1] <= 1:
        ar.append(lst[i + 1])
        mark += 1
        i += 2
    else:
        i += 1
    if mark == 2:
        tarea = tarea + ar[0] * ar[1]
        ar = []
        mark = 0
print(tarea)
