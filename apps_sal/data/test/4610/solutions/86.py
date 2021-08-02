N, K = map(int, input().split())
A = list(map(int, input().split()))
a = [0] * 200000
b = []
for i in A: a[i - 1] += 1
for i in a:
    if i: b.append(i)
b.sort()
ans = 0
for i in range(len(b) - K): ans += b[i]
print(ans)
