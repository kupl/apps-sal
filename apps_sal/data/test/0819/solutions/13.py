from sys import stdin as fin

n, k = map(int, fin.readline().split())
arr = list(map(int, fin.readline().split()))

if k >= 3:
    print(max(arr))
elif k == 1:
    print(min(arr))
else:
    print(max(arr[0], arr[-1]))
