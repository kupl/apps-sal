def initialize(arr, n):
    for i in range(n):
        arr.append(i)
    return arr


def root(arr, n):
    while arr[n] != n:
        n = arr[n]
    return n


def union(arr, a, b):
    arr[a] = arr[b]


n = int(input())
a = input()
b = input()
arr = initialize([], 26)
cnt = 0
ans = []
for i in range(n):
    a1 = ord(a[i]) - 97
    b1 = ord(b[i]) - 97
    x = root(arr, a1)
    y = root(arr, b1)
    if x != y:
        cnt += 1
        union(arr, x, y)
        ans.append([a[i], b[i]])
print(cnt)
for i in ans:
    print(i[0], i[1])
