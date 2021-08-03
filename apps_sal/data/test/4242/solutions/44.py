a, b, k = map(int, input().split())

res = 0

for i in range(100, 0, -1):
    if a % i == 0 and b % i == 0:
        res += 1
        if res == k:
            print(i)
