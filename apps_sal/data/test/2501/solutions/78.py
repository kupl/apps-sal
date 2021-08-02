N = int(input())
A = list(map(int, input().split()))

d = {}

for i in range(len(A)):
    d.setdefault(i - A[i], 0)
    d[i - A[i]] += 1
ans = 0
for i in range(len(A)):
    if d.get(i + A[i]):
        ans += d.get(i + A[i])
print(ans)
