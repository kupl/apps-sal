(n, k, x) = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
if k != 0:
    k = k % 64
else:
    k = 0
while k:
    arr.sort()
    for i in range(0, n, 2):
        arr[i] ^= x
    k -= 1
print(max(arr), min(arr))
