import sys
n = int(sys.stdin.readline())
employees = list(map(int, sys.stdin.readline().split(" ")))
days = []
curr = 0
count = 0
inside = set()
seenToday = set()
while curr < n:
    count += 1
    employee = employees[curr]
    if employee > 0:
        if employee in seenToday:
            days = []
            break
        inside.add(employee)
        seenToday.add(employee)
    else:
        if abs(employee) not in inside:
            days = []
            break
        inside.remove(abs(employee))
        if len(inside) == 0:
            days.append(count)
            count = 0
            seenToday = set()
    curr += 1

if len(days) == 0 or len(inside) > 0:
    print(-1)
else:
    print(len(days))
    for n in days:
        print(n, end=" ")
