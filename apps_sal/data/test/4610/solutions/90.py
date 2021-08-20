(n, k) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a.sort()
times = [0] * (n + 1)
for i in a:
    times[i] += 1
times.sort()
for i in range(n + 1):
    if times[i] != 0:
        j = i
        break
ans = 0
if len(times) > k - j:
    for i in range(j, len(times) - k):
        ans += times[i]
print(ans)
