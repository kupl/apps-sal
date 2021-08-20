n = int(input())
arr = list(map(int, input().split()))
st = arr[0]
ind = arr.index(max(arr))
while arr[0] < max(arr[1:]):
    arr[ind] -= 1
    arr[0] += 1
    ind = arr.index(max(arr))
if arr[0] == max(arr[1:]):
    k = arr[0] + 1
else:
    k = arr[0]
print(k - st)
