t = sorted(map(int, input().split()))
t[1] = min(t[1], t[0] * 2)
print(sum(t) // 3)

