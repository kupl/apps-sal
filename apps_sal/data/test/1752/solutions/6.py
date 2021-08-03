N = int(input())
arr = sorted(map(int, input().split()))

res = []
for i in range(N):
    if i % 2:
        res.append(arr[i])
    else:
        res.insert(0, arr[i])

print(*res)
