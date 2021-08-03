n, x = list(map(int, input().split()))
arr = list(map(int, input().split()))
if x == 0:
    print((0))
    return
sum = 0
count = 1
i = 0
while i < n:
    sum += arr[i]
    i += 1
    if sum <= x:
        count += 1
    else:
        print(count)
        return
print(count)
