n = int(input())
A = list(map(int, input().split()))
S = {}
s = 0
k = 1
for i in range(n):
    s += A[i]
    try:
        S[s] += 1
    except KeyError:
        S[s] = 1
    k = max(k, S[s])
print(n - k)
