n = int(input())
arr = list(map(int, input().split()))
tt = [0] * (n + 7)

total = 0

for a in arr:
    tt[a] += 1

for t in tt:
    total += (t * (t - 1) // 2)

for i in range(n):
    n = tt[arr[i]]
    d = (n * (n - 1) // 2) - ((n - 1) * (n - 2) // 2)
    print((total - d))
