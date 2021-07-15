x, n = list(map(int, input().split()))
p = list(map(int, input().split()))

for i in range(x+1):
    for j in [-1, 1]:
        ans = x + i*j
        if not p.count(ans):
            print(ans)
            return

