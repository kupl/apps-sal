n, m = list(map(int, input().split()))
used = [False for i in range(m)]
for i in range(n):
    amount, *lamps = list(map(int, input().split()))
    for lamp in lamps:
        used[lamp - 1] = True
if sum(used) == len(used):
    print("YES")
else:
    print("NO")


