n = int(input())
arr = list(map(int, input().split()))
count = 0
for (i, num) in enumerate(arr):
    if i == 0 or i == n - 1:
        continue
    target_arr = [arr[i - 1], arr[i], arr[i + 1]]
    if sorted(target_arr)[1] == arr[i]:
        count += 1
print(count)
