n = int(input())
(t, a) = map(int, input().split())
temp = list(map(int, input().split()))
ans = [100000.0, 1000000.0]
for (i, j) in enumerate(temp):
    if ans[1] > abs(a - (t - j * 0.006)):
        ans[0] = i + 1
        ans[1] = abs(a - (t - j * 0.006))
print(ans[0])
