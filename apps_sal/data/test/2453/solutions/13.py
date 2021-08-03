from collections import defaultdict

n = int(input())
arr = defaultdict(int)

for a0 in range(n):
    l, r = input().strip().split()
    l, r = int(l), int(r)
    arr[l] += 1
    arr[r + 1] -= 1

brr = [0] * (n + 1)

l = sorted(arr.keys())
sum = arr[l[0]]
prevpoint = l[0]

for key in l[1:]:
    brr[sum] += key - prevpoint
    prevpoint = key
    sum += arr[key]

print(*brr[1:])
