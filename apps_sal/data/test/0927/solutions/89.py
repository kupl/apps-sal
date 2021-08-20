(N, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort(reverse=True)
req = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
t = [-1] * (N + 1)
t[0] = 0
for a in A:
    q = req[a]
    for i in range(q, N + 1):
        t[i] = max(t[i], t[i - q] * 10 + a)
print(t[-1])
