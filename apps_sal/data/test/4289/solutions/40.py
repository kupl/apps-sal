n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
palace = 0
for i in range(n):
    if abs(a - t + h[i] * 0.006) < abs(a - t + h[palace] * 0.006):
        palace = i
print(palace + 1)
