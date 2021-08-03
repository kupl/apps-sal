n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
res = []
s = 0
for i in arr:
    res.append(i - s)
    s += res[-1]
    s *= -1
print(' '.join(map(str, reversed(res))))
