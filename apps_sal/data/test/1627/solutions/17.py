n = int(input())
arr = list(map(int, input().split()))
'''s = sorted(arr)
for i in range(n):
    ind = arr.index(s[i])
    for j in range(min(i, ind), max(i, ind)):
        print(j + 1, j + 2)
    arr = [arr[ind]] + arr[:ind] + arr[ind + 1:]'''
for i in range(n):
    minn = 10000000000
    ind = -1
    for j in range(i, n):
        if arr[j] < minn:
            minn = arr[j]
            ind = j
    arr = arr[:i] + [arr[ind]] + arr[i:ind] + arr[ind+1:]
    for j in range(ind - 1, i - 1, -1):
        print(j + 1, j + 2)

