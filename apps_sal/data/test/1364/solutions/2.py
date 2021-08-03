N = int(input())
arr = list(map(int, input().split()))
narr = []
last = 0
for a in arr:
    if last != a:
        narr.append(1)
        last = a
    else:
        narr[-1] += 1

res = 0
for i in range(len(narr) - 1):
    res = max(res, min(narr[i], narr[i + 1]))

print(res * 2)
