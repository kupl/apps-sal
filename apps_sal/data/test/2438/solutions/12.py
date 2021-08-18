import sys
import math
input = sys.stdin.readline

n = int(input())
s = input()
count = -s.count("AB") - s.count("BA")
s = list(s)
arr1 = [-1]
arr2 = [-1]
for i in range(n):
    if s[i] == "A":
        arr1.append(i)
    else:
        arr2.append(i)

arr1.append(n)
arr2.append(n)
for i in range(1, len(arr1) - 1):
    count += arr1[i] - arr1[i - 1] - 1
for i in range(1, len(arr2) - 1):
    count += arr2[i] - arr2[i - 1] - 1
for i in range(1, len(arr1) - 1):
    count += arr1[i + 1] - arr1[i] - 1
for i in range(1, len(arr2) - 1):
    count += arr2[i + 1] - arr2[i] - 1
print(n * (n - 1) // 2 - count)
