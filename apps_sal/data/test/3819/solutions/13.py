N = 200005
n = int(input())
k = list(map(int, input().split()))
b = list(map(int, input().split()))
p = [0 for i in range(N)]
done = 0
b.insert(0, 0)
for i in range(1, n + 1):
    p[b[i]] = i
if p[1] != 0:
    i = 2
    while p[i] == p[1] + i - 1:
        i += 1
    if p[i - 1] == n:
        j = i
        while p[j] <= j - i and j <= n:
            j += 1
        if j > n:
            print(n - i + 1)
            done = 1
mx = 0
if done == 0:
    for i in range(1, n + 1):
        mx = max(mx, p[i] - i + 1 + n)
    print(mx)
