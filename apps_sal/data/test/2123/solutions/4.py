n = int(input())
h = list(map(int, input().split()))
h = [0] + h
e = 0
res = 0
for i in range(1, n + 1):
    e += h[i - 1] - h[i]
    if e < 0:
        res += abs(e)
        e = 0
print(res)
