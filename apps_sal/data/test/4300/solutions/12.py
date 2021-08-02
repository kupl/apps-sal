n = int(input())
d = list(map(int, input().split()))
d2 = [m**2 for m in d]
print((sum(d)**2 - sum(d2)) // 2)
