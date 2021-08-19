"""
Created on Mon Mar 27 20:38:27 2017

Name: MD. Khairul Basar
Phone: 01760446942
Email: khairul.basar93@gmail.com
"""
n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
minimum = int(10000000000)
for i in range(n - 1):
    if arr[i + 1] - arr[i] < minimum:
        minimum = arr[i + 1] - arr[i]
count = 0
for i in range(n - 1):
    if arr[i + 1] - arr[i] == minimum:
        count += 1
print(minimum, count)
