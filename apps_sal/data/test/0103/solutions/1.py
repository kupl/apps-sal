n = int(input())
arr = [0] + list(map(int, input().split()))
arr.append(1001)
max_ = 0
kek = 0
for i in range(1, len(arr)):
    if arr[i] - 1 == arr[i - 1]:
        kek += 1
    else:
        max_ = max(max_, kek - 1)
        kek = 0
max_ = max(max_, kek - 1)
print(max_)

