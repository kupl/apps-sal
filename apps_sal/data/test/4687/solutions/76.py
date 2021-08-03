N, K = map(int, input().split())
c = [0] * (l := 10**5 + 1)
s = 0
for i in range(N):
    a, b = map(int, input().split())
    c[a] += b
for i in range(l):
    s += c[i]
    if s >= K:
        print(i)
        break
