a, b, k = list(map(int, input().split()))
ans = 0

counter = 0
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        counter += 1
        if counter == k:
            ans = i
            break

print(i)
