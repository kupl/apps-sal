k, r = list(map(int, input().split()))

ans = 10
for x in range(1, 11):
    mod = k * x % 10
    if mod == 0 or mod == r:
        ans = x
        break

print(ans)
