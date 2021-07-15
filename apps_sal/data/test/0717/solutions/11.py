n = int(input())
actual = 1
for _ in range(n):
    s, d = list(map(int, input().split()))
    if actual <= s:
        actual = s
    elif (actual - s) % d != 0:
        actual += (d - (actual - s) % d)
    actual += 1
print(actual-1)

