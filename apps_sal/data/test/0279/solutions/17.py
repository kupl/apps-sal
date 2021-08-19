(v1, v2) = list(map(int, input().split()))
(t, d) = list(map(int, input().split()))
print(sum((min(v1 + d * i, v2 + d * (t - i - 1)) for i in range(t))))
