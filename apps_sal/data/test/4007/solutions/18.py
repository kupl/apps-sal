n = int(input())
arr = list(map(int, input().split()))
frds = list(range(1, n + 1))
remain = set(frds) - set(arr)
slots = set()
for i in range(len(arr)):
    if arr[i] == 0:
        slots.add(i + 1)
same = slots & remain
for i in same:
    x = remain.pop()
    if x-1 != i-1:
        arr[i-1] = x
    else:
        y = remain.pop()
        arr[i-1] = y
        remain.add(x)
for i in range(len(arr)):
    if arr[i] == 0:
        arr[i] = remain.pop()
print(*arr, sep=" ")

