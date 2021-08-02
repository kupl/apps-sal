n = int(input())
alst = list(map(int, input().split()))
min_ = alst[0]
ans = 1
for a in alst[1:]:
    if a <= min_:
        ans += 1
        min_ = a
print(ans)
