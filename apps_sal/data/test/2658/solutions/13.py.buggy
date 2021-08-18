N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

now = 1
path = [1]

for i in range(N + 2):
    now = A[now]
    path.append(now)

if i >= K:
    print(path[K])
    return

now = path.pop()
lo_start = i - 1
while path[lo_start] != now:
    lo_start -= 1

loop = path[lo_start:]

ans = loop[(K - path.index(now)) % len(loop)]

print(ans)
