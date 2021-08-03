n, k = map(int, input().split())
p = list(map(int, input().split()))
q = [(x + 1) / 2 for x in p]
q1 = sum(q[:k])
ans = q1

for i in range(n - k):
    x = q1 - q[i] + q[i + k]
    q1 = x
    if ans < x:
        ans = x

print(ans)
