N = int(input())

ans = 1
prev = 0
for i in range(1, N + 1):
    count = 0
    tmp = i
    while i % 2 == 0 and 1 < i:
        count += 1
        i /= 2
    if prev < count:
        prev = count
        ans = tmp

print(ans)
