n, k = list(map(int, input().split()))
arr = [int(x) for x in input().split()]
diff = [0] * (n - 1)
p = arr[-1] - arr[0]
for i in range(n - 1):
    diff[i] = arr[i + 1] - arr[i]
diff.sort(reverse=True)
print(p - sum(diff[:k - 1]))
