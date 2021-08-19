(n, c) = map(int, input().split())
arr = [int(x) for x in input().split()]
rem = 1
last = arr[0]
for i in range(1, n):
    if arr[i] - last > c:
        rem = 1
    else:
        rem += 1
    last = arr[i]
print(rem)
