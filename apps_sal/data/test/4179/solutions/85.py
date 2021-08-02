n, m, c = list(map(int, input().split()))
arr = list(map(int, input().split()))
count2 = 0
for _ in range(n):
    count = 0
    arr2 = list(map(int, input().split()))
    for k, kk in zip(arr2, arr):
        count += k * kk
    if count + c > 0:
        count2 += 1
print(count2)
