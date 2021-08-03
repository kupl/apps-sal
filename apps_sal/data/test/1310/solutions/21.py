n = int(input())
arr = list(map(int, input().split()))
mx = 0
for i in range(len(arr)):
    t = 0
    for j in range(i, len(arr)):
        t ^= arr[j]
        mx = max(mx, t)
print(mx)
