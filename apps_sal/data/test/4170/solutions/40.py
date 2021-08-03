N = int(input())
H = list(map(int, input().split()))

res = 0
count = 0
for i, n in enumerate(H[:-1]):
    if n >= H[i + 1]:
        count += 1
        res = max(res, count)
    else:
        count = 0

print(res)
