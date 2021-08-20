(n, t) = map(int, input().split())
arr = list(map(int, input().split()))
total = t
time = 0
for i in arr[1:]:
    total += min(t, i - time)
    time = i
print(total)
