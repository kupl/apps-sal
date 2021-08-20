(n, k) = map(int, input().split())
assert n % 2 == 1
arr = sorted(map(int, input().split()))
arr = arr[n // 2:]
med = arr[0]
for i in range(1, len(arr)):
    if k == 0:
        break
    if arr[i] == med:
        continue
    else:
        diff = arr[i] - med
        kdiff = min(diff * i, k)
        med += kdiff // i
        k -= kdiff
print(med + k // len(arr))
