"""import sys
sys.stdin = open("in", "r")"""

n, k = list(map(int, input().split()))

arr = list(map(int, input().split()))

for i, j in enumerate(arr):
    if(i > 0):
        arr[i] += arr[i - 1]

sum = 0
for i in range(k - 1, n):
    nm = arr[i]
    if(i != k - 1):
        nm -= arr[i - k]
    sum += nm

print(sum / (n-k+1))

