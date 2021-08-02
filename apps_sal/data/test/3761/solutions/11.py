import collections
S = input()
x, y = list(map(int, input().split()))
f_nums = collections.defaultdict(int)
f_count = 0

for i in range(len(S)):
    if S[i] == 'F':
        f_nums[f_count] += 1
    else:
        f_count += 1

x_f = [0 for i in range(f_count + 1)]
y_f = [0 for i in range(f_count + 1)]
x_count = 0
y_count = 0
temp_sumx = 0
temp_sumy = 0
temp_sumx += f_nums[0]

for i in range(f_count + 1):
    if i == 0:
        continue

    if i % 2 == 0:
        x_f[i // 2] = f_nums[i]
        x_count += 1
    else:
        y_f[(i - 1) // 2] = f_nums[i]
        y_count += 1

x_f.sort(reverse=True)
y_f.sort(reverse=True)


for i in range(x_count):
    if abs(temp_sumx - x + x_f[i]) <= abs(temp_sumx - x - x_f[i]):
        temp_sumx += x_f[i]
    else:
        temp_sumx -= x_f[i]

for i in range(y_count):
    if abs(temp_sumy - y + y_f[i]) <= abs(temp_sumy - y - y_f[i]):
        temp_sumy += y_f[i]
    else:
        temp_sumy -= y_f[i]

if x == temp_sumx and y == temp_sumy:
    print("Yes")
else:
    print("No")
