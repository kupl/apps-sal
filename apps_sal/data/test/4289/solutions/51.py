n = int(input())
(t, a) = list(map(int, input().split()))
h = list(map(float, input().split()))
dt = 10000000
ans = 0
for i in range(len(h)):
    tmp = float(t) - 0.006 * h[i]
    if dt > abs(a - tmp):
        dt = abs(a - tmp)
        ans = i + 1
print(ans)
