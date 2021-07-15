n, k = list(map(int, input().split()))
bucket = [0] * 10 ** 5
for i in range(n):
    a, b = list(map(int, input().split()))
    bucket[a - 1] += b

sum_b = 0
for i in range(len(bucket)):
    sum_b += bucket[i]
    if sum_b >= k:
        print((i + 1))
        break

