n = int(input())
max = 0
now = 0
arr = [False for i in range(0, 2 * n)]
h = input().split(' ')
for k in range(0, 2 * n):
    if arr[int(h[k])] == False:
        arr[int(h[k])] = True
        now += 1
    else:
        now -= 1
    if max < now:
        max = now
print(max)
