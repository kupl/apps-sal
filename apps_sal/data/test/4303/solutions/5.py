n, k = list(map(int, input().split()))
x = list(map(int, input().split()))

s = 10**9

for i in range(n-k+1):
    if x[i] * x[i+k-1] >= 0:
        t = max(abs(x[i]), abs(x[i+k-1]))
    else:
        t = abs(x[i]) + abs(x[i+k-1]) + min(abs(x[i]), abs(x[i+k-1]))

    s = min(s, t)

print(s)
