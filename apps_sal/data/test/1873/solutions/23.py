n, m = map(int, input().split())
genres = list(map(int, input().split()))
q = [0] * m
for i in range(n):
    q[genres[i] - 1] += 1
print(sum(q[i] * q[j] for i in range(m) for j in range(i + 1, m)))
