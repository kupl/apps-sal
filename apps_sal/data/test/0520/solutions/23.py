"""input
1
2050
"""
n = int(input())
arr = sorted([int(i) for i in input().split()])
print(arr[len(arr) // 2])
