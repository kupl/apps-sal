n = int(input())
arr = [int(el) for el in input().split()]
arr.sort()
d_rez = []
m = 99999999
l = len(arr)
for i in range(0, l - 1):
    for j in range(i + 1, l):
        a = arr.pop(i)
        b = arr.pop(j - 1)
        size = l - 2
        diff = []
        s = 0
        for h in range(0, size, 2):
            s = s + arr[h + 1] - arr[h]
        if s < m:
            m = s
            d_rez = arr
        arr.append(a)
        arr.append(b)
        arr.sort()
print(m)
