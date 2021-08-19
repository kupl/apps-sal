(n, f) = input().split()
(n, f) = (int(n), int(f))
arr = [input().split() for i in range(n)]
arr = [(int(dayStrings[0]), int(dayStrings[1])) for dayStrings in arr]
arr = sorted(arr, key=lambda x: min(2 * x[0], x[1]) - min(x[0], x[1]), reverse=True)
res = sum((min(2 * arr[ind][0], arr[ind][1]) if ind < f else min(arr[ind][0], arr[ind][1]) for ind in range(n)))
print(res)
