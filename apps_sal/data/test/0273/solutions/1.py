import sys
a, b = list(map(str, input().split()))
arr = []
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        arr.append(a[:i] + b[:j])
arr.sort()
print(arr[0])
