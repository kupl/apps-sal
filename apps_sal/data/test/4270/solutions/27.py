n = int(input())
v = sorted(list(map(int, input().split())), reverse=True)

ans = 0
t = 1
for i in range(n - 1):
    t *= 2
    ans += v[i] / t
print(ans + v[-1] / t)
