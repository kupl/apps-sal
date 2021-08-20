(x, y, l, r) = list(map(int, input().split()))
rx = 0
while x ** rx < r:
    rx += 1
ry = 0
while y ** ry < r:
    ry += 1
arr = [l - 1, r + 1]
for i in range(rx):
    for j in range(ry):
        tmp = x ** i + y ** j
        if l <= tmp <= r:
            arr.append(tmp)
arr = list(sorted(set(arr)))
ans = 0
for i in range(1, len(arr)):
    ans = max(ans, arr[i] - arr[i - 1] - 1)
print(ans)
