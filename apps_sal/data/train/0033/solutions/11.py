from math import ceil
n = int(input())
for _ in range(n):
    k = int(input())
    arr = list(range(1, k + 1))
    o = []
    for i in range(k - 1):
        a = arr.pop()
        b = arr.pop()
        o.append((a, b))
        arr.append(ceil((a + b) / 2))
    print(arr[0])
    for i in range(len(o)):
        print(o[i][0], o[i][1])
