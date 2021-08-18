import sys

n, m = list(map(int, input().split()))

arr = list(map(int, input().split()))

for line in sys.stdin:
    l, r, x = list(map(int, line.split()))
    cnt = 0
    for i in range(l - 1, r):
        if arr[i] < arr[x - 1]:
            cnt += 1
    if cnt == x - l:
        print("Yes")
    else:
        print("No")
