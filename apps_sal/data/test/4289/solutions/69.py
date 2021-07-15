n = int(input())
t, a = map(int, input().split())
h = [int(s) for s in input().split()]

min_abs = 100000
index = 0
for i in range(n):
    temp = t - h[i] * 0.006
    if abs(a - temp) < min_abs:
        min_abs = abs(a - temp)
        index = i
print(index + 1)
