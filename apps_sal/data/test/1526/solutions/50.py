a = list(map(int, input().split()))
m = max(a)
t = 0
if (m * 3 - sum(a)) % 2 == 1: t = 3
print(((m * 3 - sum(a) + t) // 2))
