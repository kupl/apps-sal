a, ta = list(map(int, input().split()))
b, tb = list(map(int, input().split()))
hour, minutes = list(map(int, input().split(':')))
time_dep = hour * 60 + minutes - 300
count = 0
for i in range(0, 1140, b):
    if i + tb > time_dep and i < time_dep + ta:
        count += 1
        #print(i, i + tb, count)
print(count)

