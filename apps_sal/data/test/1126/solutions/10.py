n, x, m = list(map(int, input().split()))
A = []
ls = [0] * (m + 1)
start = 0
cycle_sum = 0
cnt = 0
while ls[x] == 0:
    A.append(x)
    cycle_sum += x
    ls[x] = cnt
    cnt += 1
    x = (x * x) % m

if n <= cnt:
    ans = 0
    for i in range(0, n): ans += A[i]
    print(ans)
    return
cycle = 0
rest = cnt - ls[x]
for i in range(ls[x], cnt):
    cycle += A[i]
n -= cnt
ans = cycle_sum
ans += (n // rest) * cycle
n %= rest
si = ls[x]
for i in range(n):
    ans += A[si + i]
print(ans)
