N = int(input())
A = sorted([(int(x[1]), x[0]) for x in enumerate(input().split())], reverse=True)


V = [0]

for i in range(N - 1):
    a, p = A[i]
    s = i + 1
    V2 = [None] * (s + 1)

    for t in range(s + 1):
        v = 0

        if t > 0:
            v = V[t - 1] + a * abs(p - (t - 1))

        if t < s:
            v = max(V[t] + a * abs(p - (N - s + t)), v)

        V2[t] = v

    V = V2

a, p = A[-1]
for i in range(N):
    V[i] += a * abs(p - i)

print((max(V)))
