n = int(input())
ans = 0
for x in range(1, n + 1):
    if x % 3 == 0 or x % 5 == 0:
        continue
    ans += x
print(ans)
