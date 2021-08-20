3
n = int(input())
d = list(map(int, input().split()))
(s, t) = tuple(map(int, input().split()))
if s > t:
    (s, t) = (t, s)
a1 = sum([d[i] for i in range(s - 1, t - 1)])
a2 = sum([d[i] for i in range(s - 2, t - n - 2, -1)])
print(min(a1, a2))
