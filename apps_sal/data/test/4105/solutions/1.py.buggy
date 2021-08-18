import sys

n, k = list(map(int, input().split()))

if n > k * (k - 1):
    print("NO")
    return
else:
    print("YES")

count = 0
for i in range(1, k):
    for j in range(1, k + 1):
        print(j, (j + i - 1) % k + 1)
        count += 1

        if count == n:
            break
    if count == n:
        break
