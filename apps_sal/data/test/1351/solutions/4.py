l, r = [int(i) for i in input().split()]

for i in range(l, r + 1):
    s = list(str(i))
    sl = set(s)
    if len(s) == len(sl):
        print(i)
        return

print(-1)
