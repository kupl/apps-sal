(a, b) = map(int, input().split())
cnt = 0
tap = 1
while tap < b:
    tap = tap + (a - 1)
    cnt = cnt + 1
print(cnt)
