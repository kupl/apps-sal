n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

new_arr = []
for i in range(n - 1):
    new_arr.append(arr[i + 1] - arr[i])

new_arr.sort()
print(sum(new_arr[:n - k]))
