n = int(input())
arr = sorted(map(int, input().split()))
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
arr = sorted(freq.keys())

j = 0
curr = 0
while j < len(arr) and abs(arr[j] - arr[0] <= 5):
    curr += freq[arr[j]]
    j += 1

i = 1
ans = curr
while i < len(arr):
    curr -= freq[arr[i - 1]]
    while j < len(arr) and abs(arr[j] - arr[i] <= 5):
        curr += freq[arr[j]]
        j += 1
    ans = max(ans, curr)
    i += 1
print(ans)
