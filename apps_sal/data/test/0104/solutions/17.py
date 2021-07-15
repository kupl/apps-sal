N = int(input())
arr = list(map(int, input().split()))
S = sum(arr)
cur = 0
idx = 0

for item in arr:
    cur += item
    idx += 1
    if (cur >= S/2):
        print(idx)
        break


