n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

i = 0
kv = 1
rest = k
while i <= n - 2:
    dist = arr[i + 1] - arr[i]
    if rest < dist:
        kv += 1
        rest = k
    if dist > k:
        kv = -1
        break
    while rest >= arr[i + 1] - arr[i]:
        rest -= arr[i + 1] - arr[i]
        i += 1
        if i == n - 1:
            break

print(kv)
