n = int(input())
t = list(map(int, input().split()))
(a, b) = (min(t), max(t))
n = t.count(a)
if a == b:
    print(0, n * (n - 1) // 2)
else:
    print(b - a, n * t.count(b))
