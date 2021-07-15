n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
arr = [abs(arr[i] - arr[i + 1]) for i in range(n - 1)]
d = min(arr)
c = arr.count(d)

print(d, c)

