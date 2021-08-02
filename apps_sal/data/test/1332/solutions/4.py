a = list(map(int, input().split()))
if (sum(a) % len(a) == 0) and (sum(a) != 0):
    print(sum(a) // len(a))
else:
    print(-1)
