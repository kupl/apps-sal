n = list(map(int, input().strip().split()))[0]
arr = list(map(int, input().strip().split()))

count = dict()
for i in arr:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

maximum = 0
for key in count:
    if count[key] > maximum:
        maximum = count[key]

print(maximum)
