(a, b, k) = map(int, input().split())
count = 0
for i in range(a, 0, -1):
    if a % i == 0 and b % i == 0:
        count += 1
    if count == k:
        print(i)
        break
