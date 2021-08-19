n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
diffs = []
for i in range(1, n):
    if arr[i] != arr[i - 1]:
        diffs.append(arr[i] - arr[i - 1])
diffs = list(reversed(sorted(diffs)))

ans = sum(diffs)

# print(diffs)

for i in range(min(len(diffs), k - 1)):
    ans -= diffs[i]

print(ans)
