(n, m) = map(int, input().split())
xl = list(map(int, input().split()))
xl.sort()
difl = []
for i in range(1, m):
    difl.append(xl[i] - xl[i - 1])
difl.sort(reverse=True)
if n >= m:
    ans = 0
else:
    ans = xl[-1] - xl[0] - sum(difl[:n - 1])
print(ans)
