n, k = list(map(int, input().split()))
x = list(map(int, input().split()))

mt = 5 * 10**8

for i in range(n - k + 1):
    mt = min(mt, 2 * abs(x[i]) + abs(x[i + k - 1]), abs(x[i]) + 2 * abs(x[i + k - 1]))

if x[0] > 0:
    mt = min(mt, x[k - 1])
elif x[-1] < 0:
    mt = min(mt, abs(x[-1 - k + 1]))
print(mt)
