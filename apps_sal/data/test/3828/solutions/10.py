def readInts(): return list(map(int, input().split()))


n = int(input())
a = readInts()
p = [0] * n
for i in range(n):
    p[a[i] - 1] = i
inc = 1
ret = n - 1
# print(p)
for i in range(1, n):
    if p[i] > p[i - 1]:
        inc += 1
    else:
        inc = 1
    ret = min(ret, n - inc)
print(ret)
