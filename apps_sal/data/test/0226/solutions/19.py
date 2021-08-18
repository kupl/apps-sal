N = int(input())
n = list(map(int, input().split(" ")))

if N == 1:
    ans = [0, n[0]]
elif N == 2:
    ans = [min(n), max(n)]
else:
    n.reverse()
    f = max(n[0], n[1])
    s = n[0] + n[1]
    for i in range(2, N):
        f = max(n[i] + s - f, f)
        s += n[i]
    ans = [s - f, f]

print(" ".join(map(str, ans)))
