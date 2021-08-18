n, k = list(map(int, input().split()))
p = list(map(int, input().split()))


def ev(n):
    return n * (n + 1) / (2 * n)


q = [0]
for i in range(n):
    q.append(ev(p[i]))
    q[i + 1] = q[i] + ev(p[i])

tmp = 0
for j in range(n - k + 1):
    if tmp <= q[j + k] - q[j]:
        tmp = q[j + k] - q[j]
print(tmp)
