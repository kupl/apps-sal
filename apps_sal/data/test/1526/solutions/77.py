a = list(map(int, input().split()))
t = max(a) * 3 - sum(a)
print(t // 2 + (t % 2) * 2)
