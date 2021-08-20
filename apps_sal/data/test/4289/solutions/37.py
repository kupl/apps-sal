n = int(input())
(t, a) = list(map(int, input().split()))
h = list(map(int, input().split()))
res = 0
val = 10 ** 5
for i in range(n):
    if (v := abs(a - (t - h[i] * 0.006))) < val:
        val = v
        res = i + 1
print(res)
