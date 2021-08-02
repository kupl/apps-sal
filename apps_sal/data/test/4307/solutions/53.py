def countDivisor(x):
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    return count


N = int(input())
ans = 0

for i in range(1, N + 1, 2):
    if countDivisor(i) == 8:
        ans += 1
print(ans)
