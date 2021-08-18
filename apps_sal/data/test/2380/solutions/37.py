n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
Q = []
for i in range(m):
    b, c = list(map(int, input().split()))
    Q.append([b, c])

Q = sorted(Q, key=lambda x: x[1], reverse=1)
kae = 0

d = [-1] * (n)
now = 0
for l in Q:
    b, c = l
    if n - now < b:
        d[now:] = [c] * (n - now)
        break
    d[now:now + b] = [c] * b
    now += b

ans = sum(A)
now = ans
for kae in range(1, n + 1):
    now += d[kae - 1]
    now -= A[kae - 1]
    ans = max(ans, now)
print(ans)
