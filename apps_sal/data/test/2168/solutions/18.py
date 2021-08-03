n = int(input())

m = n * [0]
for i in range(n):
    en = list(map(int, input().split()))
    m[i] = en[1:]

max_line_index = 0
maximum = m[0][0]

for i in range(n):
    for j in range(len(m[i])):
        if(m[i][j] > maximum):
            maximum = m[i][j]
            max_line_index = i

increase = 0

for i in range(n):
    if(i != max_line_index):
        cur_max = max(m[i])
        increase += ((maximum - cur_max) * len(m[i]))

print(increase)
