point = {}
n = int(input())
for i in range(n):
    (l, r) = map(int, input().split())
    r += 1
    if l not in point:
        point[l] = 0
    if r not in point:
        point[r] = 0
    point[l] += 1
    point[r] -= 1
line = []
for key in point:
    line.append((key, point[key]))
line.sort()
ans = [0] * (n + 1)
last_index = 0
last_value = 0
for (index, value) in line:
    ans[last_value] += index - last_index
    last_index = index
    last_value += value
for cnt in ans[1:]:
    print(cnt, end=' ')
