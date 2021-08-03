n = int(input())
t, a = map(int, input().split())
data = list(map(int, input().split()))
ans = 0
for i in range(n):
    if abs(t - data[i] * 0.006 - a) < abs(t - data[ans] * 0.006 - a):
        ans = i
print(ans + 1)
