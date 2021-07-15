n = int(input())
arr = list(map(int, input().split()))
arr1 = [arr[0]]
m = -1
for i, v in enumerate(arr):
    if v > m + 1:
        print(i+1)
        break
    m = max(m, v)
else:
    print(-1)


