n, t = map(int, input().split())
arr = list(map(int, input().split()))
summ = t
for i in range(n - 1):
    summ += min(t, arr[i + 1] - arr[i])
print(summ)
