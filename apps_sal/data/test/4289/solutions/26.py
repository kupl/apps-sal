n = int(input())
(t, a) = map(int, input().split())
h = list(map(int, input().split()))
b = 10 ** 5
c = 0
for i in range(len(h)):
    if abs(t - h[i] * 0.006 - a) < b:
        b = abs(t - h[i] * 0.006 - a)
        c = i
print(c + 1)
