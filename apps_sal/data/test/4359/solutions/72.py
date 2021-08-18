ar = []
for i in range(5):
    ar.append(int(input()))
arr = [10 - i % 10 for i in ar]
for i in range(5):
    if arr[i] == 10:
        arr[i] = 0
last = arr.index(max(arr))
time = 0
for i, x in enumerate(ar):
    if i != last:
        time += x + arr[i]
time += ar[last]
print(time)
