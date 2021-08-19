n = int(input())
(t, a) = map(int, input().split())
h = list(map(int, input().split()))
candidate = float('inf')
ans = 0
for i in range(n):
    temp = t - h[i] * 0.006
    difference = abs(a - temp)
    if difference < candidate:
        candidate = difference
        ans = i + 1
print(ans)
