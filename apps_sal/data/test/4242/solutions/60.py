(a, b, k) = list(map(int, input().split()))
maxint = max(a, b)
cnt = 0
for i in range(maxint, 0, -1):
    if a % i == 0 and b % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
