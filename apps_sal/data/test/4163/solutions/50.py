def cin():
    return list(map(int, input().split()))


label = 'No'
times = int(input())
count = 0
for i in range(times):
    zorome = cin()
    if zorome[0] == zorome[1]:
        count += 1
    else:
        count = 0
    if count == 3:
        label = 'Yes'
print(label)
