import sys

n, a = list(map(int, input().split()))

arr = list(map(int, input().split()))

i, j = a - 1, a - 1

c = 0

if arr[i]:
    c += 1

while i >= 0 or j < n:
    i -= 1
    j += 1
    if i >= 0 and j < n and arr[i] == arr[j] == 1:
        c += 2
    elif i >= 0 and j >= n and arr[i]:
        c += 1
    elif i < 0 and j < n and arr[j]:
        c += 1

print(c)
sys.stdout.flush()

