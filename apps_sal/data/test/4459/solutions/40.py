n = int(input())
a = list(map(int, input().split()))
d = dict()
for i in a:
    if i not in d:
        d[i] = 1

    else:
        d[i] += 1
count = 0
for key, value in list(d.items()):
    if int(key) > value:
        count += int(value)
    elif int(key) < value:
        count += value - int(key)

print(count)
