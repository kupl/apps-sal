(n, k) = map(int, input().split())
arr = [int(i) for i in input().split()]
i = 0
j = 1
s = 0
while i != n - 1:
    f = 0
    while j != n and arr[j] - arr[i] <= k:
        f += 1
        j += 1
    if f != 0:
        i = j - 1
        s += 1
    else:
        s = -1
        break
print(s)
