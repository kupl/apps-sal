n = int(input())
q = [0] * n
for i in range(n - 1):
    (u, v) = list(map(int, input().split()))
    q[u - 1] += 1
    q[v - 1] += 1
print(q.count(1))
