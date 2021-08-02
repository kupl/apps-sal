n = int(input())
t, a = map(int, input().split())
temp = list(map(int, input().split()))
ans = [1e5, 1e6]
for i, j in enumerate(temp):
    if ans[1] > abs(a - (t - j * 0.006)):
        ans[0] = i + 1
        ans[1] = abs(a - (t - j * 0.006))
print(ans[0])
