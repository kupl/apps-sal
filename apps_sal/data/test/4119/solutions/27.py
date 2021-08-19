(n, m) = map(int, input().split())
x = sorted(list(map(int, input().split())))
N = []
for i in range(m - 1):
    N.append(abs(x[i + 1] - x[i]))
N.sort(reverse=True)
print(sum(N[n - 1:]))
