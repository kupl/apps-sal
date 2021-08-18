

h, n = map(int, input().split())
damage = list(map(int, input().split()))

if h - sum(damage) <= 0:
    print("Yes")
else:
    print("No")
