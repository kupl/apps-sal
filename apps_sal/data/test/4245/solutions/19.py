a, b = map(int, input().split())
ans = 1
count = 0
while ans < b:
    count += 1
    ans += a - 1
print(count)
