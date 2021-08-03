a, b, k = map(int, input().split())

count = 0
n = min(a, b)

for i in reversed(range(1, n + 1)):
    if a % i == 0 and b % i == 0:
        count += 1
        if count == k:
            ans = i

print(ans)
