n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
ans = 1
temp = t - h[0] * 0.006
for i in range(n):
    loc = t - h[i] * 0.006
    if abs(a - loc) < abs(a - temp):
        temp = loc
        ans = i + 1
print(ans)
