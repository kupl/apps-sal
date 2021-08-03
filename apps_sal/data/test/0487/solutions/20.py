n = int(input())
xs = list(map(int, input().split()))
max_x = max(xs)
bad = sum(xs)
good = sum(max_x - x for x in xs)
ans = 0
while True:
    if ans * n + good > bad:
        print(ans + max_x)
        break
    ans += 1
