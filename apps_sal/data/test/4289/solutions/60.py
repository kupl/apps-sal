n = int(input())
(t, a) = map(int, input().split())
h = list(map(int, input().split()))
b = list(map(lambda h: abs(a - (t - h * 0.006)), h))
print(b.index(min(b)) + 1)
