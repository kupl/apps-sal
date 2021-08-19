(p, q, l, r) = input().split()
fixed = []
for i in range(int(p)):
    endpoints = input().split()
    for j in range(int(endpoints[0]), int(endpoints[1]) + 1):
        fixed += [j]
temp = []
for i in range(int(q)):
    endpoints = input().split()
    for j in range(int(endpoints[0]), int(endpoints[1]) + 1):
        temp += [j]
count = 0
for time in range(int(l), int(r) + 1):
    new_temp = temp[:]
    new_temp = [i + time for i in new_temp]
    for i in new_temp:
        if i in fixed:
            count += 1
            break
print(count)
