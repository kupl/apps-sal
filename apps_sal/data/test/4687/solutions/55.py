n, k = map(int, input().split())
num, count = [0] * ((10**5) + 1), 0
for _ in range(n):
    a, b = map(int, input().split())
    num[a] += b
for i in range(len(num)):
    count += num[i]
    if count >= k:
        print(i)
        break
