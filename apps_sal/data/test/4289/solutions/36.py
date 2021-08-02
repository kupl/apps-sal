n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
x = 10**6
total = 0
for i in range(n):
    if abs(x - a) > abs(t - h[i] * 0.006 - a):
        x = t - h[i] * 0.006
        total = i + 1
print(total)
