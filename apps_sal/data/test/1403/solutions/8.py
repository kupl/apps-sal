(n, k) = list(map(int, input().strip().split(' ')))
brr = list(map(int, input().strip().split(' ')))
arr = list(set(brr))
arr.sort(reverse=True)
n = len(arr)
for i in range(n - 2, -1, -1):
    if arr[i] <= arr[i + 1] + k:
        arr[i + 1] = -1
ans = [0 for i in range(1000001)]
for i in arr:
    if i != -1:
        ans[i] += 1
an = []
for i in brr:
    if ans[i] != 0:
        an.append(i)
print(len(an))
