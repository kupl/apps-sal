n = int(input())
t, a = list(map(int, input().split()))
h = [int(x) for x in input().split()]

ans = float('inf')
x = 0
for i in range(n):
    now = t - h[i] * 0.006
    if abs(now - a) < ans:
        ans = abs(now - a)
        x = i + 1
print(x)
