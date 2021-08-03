n = int(input())
employees = input().split(" ")
employees_changed = []
for i in range(0, len(employees)):
    employees_changed.append(int(employees[i]))

ans = [0] * (n + 1)
for x in employees_changed:
    ans[x] += 1

for i in range(1, n + 1, 1):
    print((ans[i]))
# Compotitive Programming
