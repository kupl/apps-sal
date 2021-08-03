k = int(input())
count = 0
n = 0
for i in range(k):
    n = (10 * n + 7) % k
    if n % k == 0:
        print(i + 1)
        count += 1
        break
if count == 0:
    print(-1)
