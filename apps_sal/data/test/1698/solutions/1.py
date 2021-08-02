n, k = list(map(int, input().split()))
f = list(map(int, input().split()))

f.sort()
res = 0

while len(f) > 0:
    res += 2 * f[-1] - 2
    for i in range(k):
        if len(f) > 0:
            f.pop()

print(res)
