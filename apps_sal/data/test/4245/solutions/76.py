a, b = map(int, input().split())

ans = 0
tap = 1
while tap < b:
    tap += a - 1
    ans += 1

print(ans)
