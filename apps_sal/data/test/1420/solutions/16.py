line = input().split(' ')
n = int(line[0])
l = int(line[1])
line = input().split(' ')
lst = []
for item in line:
    lst.append(int(item))
lst.sort()
maxdiff = max(l - lst[n - 1], lst[0]) * 2
for i in range(n - 1):
    diff = lst[i + 1] - lst[i]
    if diff > maxdiff:
        maxdiff = diff
print(str(maxdiff / 2.0))
