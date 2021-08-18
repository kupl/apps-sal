from collections import defaultdict
total = 0


def update(ft, pos, val):
    nonlocal total
    total += 1
    while pos < len(ft):
        ft[pos] += val
        pos += pos & (-pos)


def query(ft, pos):
    ans = 0
    while pos > 0:
        ans += ft[pos]
        pos -= pos & (-pos)
    return ans


n = int(input())
arr = list(map(lambda x: int(x), input().split()))
freCount = defaultdict(int)
leftCount = []
rightCount = []
ans = 0
ft = [0] * (n + 10)

for i in range(n):
    if arr[i] in freCount:
        freCount[arr[i]] += 1
    else:
        freCount[arr[i]] = 1
    leftCount.append(freCount[arr[i]])

freCount = defaultdict(int)

for i in range(n - 1, -1, -1):
    if arr[i] in freCount:
        freCount[arr[i]] += 1
    else:
        freCount[arr[i]] = 1
    update(ft, freCount[arr[i]], 1)
    rightCount.append(freCount[arr[i]])

rightCount = rightCount[::-1]

for i in range(n):
    update(ft, rightCount[i], -1)
    ans += query(ft, leftCount[i] - 1) if leftCount[i] > 1 else 0

print(ans)
